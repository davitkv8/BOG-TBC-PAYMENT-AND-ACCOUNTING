from pydantic import BaseModel
from datetime import datetime


class PaymentData(BaseModel):
    to_acc: str
    from_acc: str
    doc_num: int
    amount: float
    additional_description: str
    description: str


class BalanceSchema(BaseModel):

    bank: str
    account_number: int
    balance: int
    currency: str
    synced_at_date: datetime

    class Config:
        orm_mode = True
