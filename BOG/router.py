from datetime import date
from fastapi import APIRouter
from .bog_api import BogApi


router = APIRouter()
bog_api = BogApi()


# Generate Token
@router.get("/bog_token/")
async def bog_token() -> str:
    return bog_api.bog_token()


# Balance
@router.get("/bog_balance/{account_number}/{currency}/")
async def current_balance(account_number: str, currency: str):
    return bog_api.current_balance(account_number, currency)


# Transactions
@router.get("/bog_transactions/{account_number}/{currency}/{start_date}/{end_date}")
async def bog_transactions(account_number: str, currency: str,
                           start_date: date, end_date: date) -> list:

    return bog_api.transactions(account_number, currency, start_date, end_date)
