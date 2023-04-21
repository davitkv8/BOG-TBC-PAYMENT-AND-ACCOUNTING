import requests
import base64
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()


class BogApi:
    def __init__(self):
        self.grant_type = os.environ.get("grant_type")
        self.client_id = os.environ.get("client_id")
        self.client_secret = os.environ.get("client_secret")
        self.scope = os.environ.get("scope")

    def bog_token(self):
        url = 'https://account.bog.ge/auth/realms/bog/protocol/openid-connect/token'

        payload = f'grant_type={self.grant_type}&client_id=' \
                  f'{self.client_id}&client_secret={self.client_secret}&scope={self.scope}'

        basic_authorization = base64.b64encode(
            ('Basic' + self.client_id + ':' + self.client_secret).encode("utf-8")
        )

        headers = {
            'Authorization': basic_authorization,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # Make the request
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            print("Success!")
        else:
            print("Error:", response.status_code, response.text)
            raise HTTPException(status_code=400, detail="ტოკენის დაგენერირება ვერ მოხდა!")

        access_token = response.json()["access_token"]

        return access_token

    def current_balance(self, account_number: str, currency: str) -> tuple:
        token = self.bog_token()
        headers = {
            'Authorization': f'Bearer {token}'
        }
        url = f"https://api.businessonline.ge/api/accounts/{account_number}/{currency}"

        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            print("Success!")
        else:
            raise HTTPException(status_code=400, detail="ვერ მოხერხდა მიმდინარე ბალანსის წამოღება!")

        return response.json()['CurrentBalance'], account_number, currency

    def transactions(self, account, currency, start_date, end_date):
        url = f"https://api.businessonline.ge/api/statement/" \
              f"{account}/{currency}/{start_date}/{end_date}"

        token = self.bog_token()
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            print("Success!")
        else:
            raise HTTPException(status_code=400, detail="ვერ მოხერხდა ტრანზაქციების წამოღება!")
        return response.json()['Records']
