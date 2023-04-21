import os
import requests


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
