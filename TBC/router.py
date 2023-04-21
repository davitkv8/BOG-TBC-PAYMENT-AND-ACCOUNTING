from fastapi import APIRouter
from datetime import datetime
from .tbc_api import (
    TbcApiExternal
)
from .schemas import PaymentData


router = APIRouter()


# @router.post("/tbc_transfer_within_bank/")
# def tbc_transfer_within_bank(data: PaymentData) -> str:
#     data_dict = data.dict()
#     # return bog_api.bog_token()


@router.post("/tbc_transfer_to_own_acc/")
def tbc_transfer_to_own_acc(data: PaymentData) -> dict:
    data_dict = data.dict()
    return TbcApiExternal.transfer_to_own_account(**data_dict)
