from fastapi import APIRouter
from datetime import datetime
from .tbc_api import (
    get_balance_data_from_db,
    get_movements, TbcApiExternal
)
from .schemas import PaymentData


router = APIRouter()


@router.get("/tbc_movements/")
def tbc_movements(
        start_datetime: str = datetime.now().replace(
            hour=0, minute=0, second=0
        ).strftime('%Y-%m-%d %H:%M:%S'),

        end_datetime: str = datetime.now().replace(
            hour=23, minute=59, second=59
        ).strftime('%Y-%m-%d %H:%M:%S')

) -> list:
    """
        :param start_datetime: accepts datetime string (yyyy-mm-dd H:M:S)
        :param end_datetime: accepts datetime string (yyyy-mm-dd H:M:S).
        :return: returns result from our database, found in that range.
    """

    return get_movements(start_datetime, end_datetime)


@router.get("/tbc_statement/")
def tbc_balance() -> list:
    return get_balance_data_from_db()


# @router.post("/tbc_transfer_within_bank/")
# def tbc_transfer_within_bank(data: PaymentData) -> str:
#     data_dict = data.dict()
#     # return bog_api.bog_token()


@router.post("/tbc_transfer_to_own_acc/")
def tbc_transfer_to_own_acc(data: PaymentData) -> dict:
    data_dict = data.dict()
    return TbcApiExternal.transfer_to_own_account(**data_dict)
