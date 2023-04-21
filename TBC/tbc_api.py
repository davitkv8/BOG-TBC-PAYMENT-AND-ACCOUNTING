import datetime
import os

import requests
import xml.etree.ElementTree as ET

from datetime import date, datetime, timedelta

from namings import (
    TBC_MOVEMENT_API_FIELD_NAMINGS,
    NESTED_XML_TAGS,
    ACCOUNTS_DATA
)

from database import SessionLocal
from .models import Balance, Movement
from .xml_payloads import *


class TbcApiExternal:
    def __init__(self):
        self.cert_path = os.environ.get("CERT_PATH")
        self.key_path = os.environ.get("KEY_PATH")
        self.cert_file = os.environ.get("PFX_FILE")
        self.__default_user = os.environ.get("DEFAULT_USER")
        self.__password = os.environ.get("USER_PASSWORD")

        # Just use this headset as prefix
        self.headset = ".//{http://www.mygemini.com/schemas/mygemini}"

    def get_balance(self):

        db = SessionLocal()

        url, headers, payload = TBC_ACCOUNT_STATEMENT_PAYLOAD.values()
        to_date_str = date.today().strftime("%Y-%m-%d")

        data = []

        for address in ACCOUNTS_DATA.keys():

            formatted_payload = payload.format(
                self.__default_user, self.__password,
                1111, to_date_str, address, "GEL"
            )

            response = requests.post(
                url, data=formatted_payload, headers=headers,
                cert=(self.cert_path, self.key_path), verify=True
            )

            xml_response = response.content.decode('ascii')

            root = ET.fromstring(xml_response)

            closing_balance = root.find(self.headset + "closingBalance").text

            obj = Balance(**{
                "bank": "TBC",
                "currency": "GEL",
                "account_number": address,
                "balance": closing_balance,
            })

            data.append(obj)

        db.add_all(data)
        db.commit()

        return f"Successfully got and saved balance data to local db."

    def parse_xml_to_dict_and_get_incomes(self, xml_data):

        converted_dict_data = [

        ]

        root = ET.fromstring(xml_data)
        movements = root.findall(self.headset + "accountMovement")

        for movement in movements:
            # Check if transaction type is "income".
            # The income is represented as '20' in TBC API DOC.
            # We're only looking for that case.
            if movement.find(self.headset + "transactionType").text == '20':
                record = {}
                # get all fields we are interested in
                for field_name_in_api, field_name_in_db in TBC_MOVEMENT_API_FIELD_NAMINGS.items():
                    field_name_in_api = field_name_in_api.split(":")[1]

                    value = movement.find(self.headset + field_name_in_api)

                    if field_name_in_api in NESTED_XML_TAGS:
                        value = value.find(self.headset + field_name_in_api)

                    try:
                        record.update({
                            field_name_in_db: value.text
                        })
                    except AttributeError:
                        record.update({
                            field_name_in_db: None
                        })

                converted_dict_data.append({
                    record['external_payment_id']: record
                })

        return converted_dict_data

    def filter_refine_save_movements_data(self, data):

        # Filter current transactions in 7 days range
        # Just for self insurance (only current day is enough in general purposes)
        start_date = date.today() - timedelta(days=6)
        end_date = date.today() + timedelta(days=1)

        db = SessionLocal()

        identifier_ids_in_api_of_our_data = db.query(Movement.external_payment_id).filter(
            Movement.document_date.between(start_date, end_date)
        )

        identifier_ids_in_api_of_our_data = set(
            identifier_id[0] for identifier_id in identifier_ids_in_api_of_our_data
        )

        bulk_create_filtered_data = []

        for transaction in data:
            for api_id, value in transaction.items():

                # Filter out data, which already exists in our database
                if int(api_id) in identifier_ids_in_api_of_our_data:
                    continue

                value['document_date'] = value['document_date'].split("T")[0]

                bulk_create_filtered_data.append(Movement(**value))

        db.add_all(bulk_create_filtered_data)
        db.commit()

        return f"CREATED {bulk_create_filtered_data.__len__()} new records"

    def get_movements(self, *args):
        url, headers, payload = TBC_MOVEMENTS_PAYLOAD.values()

        start_date = end_date = datetime.today().date().strftime(
            "%Y-%m-%d"
        )

        start_date = start_date.replace("18", "12")
        end_date = end_date.replace("18", "19")

        start_date = (lambda x: x + 'T00:00:00.000')(start_date)
        end_date = (lambda x: x + 'T23:59:59.999')(end_date)

        formatted_payload = payload.format(
            self.__default_user, self.__password,
            111, start_date, end_date
        )

        response = requests.post(
            url, data=formatted_payload, headers=headers,
            cert=(self.cert_path, self.key_path), verify=True
        )

        data = response.content.decode('utf-8')
        data = self.parse_xml_to_dict_and_get_incomes(data)
        data = self.filter_refine_save_movements_data(data)

        return data

    def transfer_to_own_account(self, **kwargs):
        url, headers, payload = TBC_OWN_ACC_PAYMENT_PAYLOAD.values()

        formatted_payload = payload.format(
            ACCOUNTS_DATA.get(kwargs['from_acc']), self.__password,
            1111, *kwargs.values()
        )

        response = requests.post(
            url, data=formatted_payload, headers=headers,
            cert=(self.cert_path, self.key_path), verify=True
        )

        xml_data = response.content.decode('utf-8')

        root = ET.fromstring(xml_data)
        response_content = {
            "message": "successfully transferred!",
            "payment_id": root.find(self.headset + "paymentId").text
        }

        return response_content


def get_balance_data_from_db(*args):
    db = SessionLocal()
    now = datetime.now()
    start_time = now - timedelta(hours=1)

    result = db.query(Balance).filter(
        Balance.synced_at_datetime > start_time
    ).all()

    return result


def get_movements(*args):
    db = SessionLocal()

    start_datetime, end_datetime = tuple(
        map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'), args)
    )

    result = db.query(Movement).filter(
        Movement.synced_at_datetime > start_datetime,
        Movement.synced_at_datetime < end_datetime
    ).all()

    return result
