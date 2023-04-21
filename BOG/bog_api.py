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