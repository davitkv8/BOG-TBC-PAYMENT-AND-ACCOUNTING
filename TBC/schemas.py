from schwifty import IBAN
from pydantic import BaseModel, Field, validator
from datetime import datetime


class OwnAccPaymentData(BaseModel):
    to_acc: str
    from_acc: str
    doc_num: int
    amount: float
    additional_description: str
    description: str


class WithinBankPaymentData(BaseModel):
    to_acc: str

    from_acc: str  # if you always transfer money from same acc,
    # use Field() with value='my_acc' and const=True.

    doc_num: int
    amount: float
    additional_description: str
    description: str = Field('გადარიცხვა', const=True)
    beneficiary_name: str
    beneficiary_tax_code: str

    @validator('beneficiary_tax_code')
    def validate_beneficiary_tax_code_length(cls, value):
        if len(value) not in (9, 11):
            raise ValueError("Beneficiary tax code length should be 9 or 11 characters")
        return value

    @validator('amount')
    def validate_amount(cls, value):
        if value < 0:
            raise ValueError("Amount must be positive number.")
        return value

    @validator('to_acc')
    def validate_account_address(cls, value):
        try:
            iban = IBAN(value)
            if iban.bank_code not in ["BG", "TB"]:
                raise ValueError("IBAN check failed.")
            return value

        except Exception as e:
            raise e


class BalanceSchema(BaseModel):

    bank: str
    account_number: int
    balance: int
    currency: str
    synced_at_date: datetime

    class Config:
        orm_mode = True
