import datetime as _dt
import sqlalchemy as _sql
from database import Base


class Movement(Base):
    __tablename__ = "movement"

    id = _sql.Column(_sql.BigInteger, primary_key=True, index=True)
    movement_id = _sql.Column(_sql.Double, index=True)
    external_payment_id = _sql.Column(_sql.BigInteger, index=True, unique=True)
    debit_credit = _sql.Column(_sql.String, index=True)

    synced_at_datetime = _sql.Column(_sql.DateTime, default=_dt.datetime.now)
    document_date = _sql.Column(_sql.Date, index=False)

    description = _sql.Column(_sql.String, index=False)
    amount = _sql.Column(_sql.Double, index=True)
    currency = _sql.Column(_sql.String, index=False)

    sc_account_number = _sql.Column(_sql.String, index=False)
    sc_account_name = _sql.Column(_sql.String, index=False)
    additional_info = _sql.Column(_sql.String, index=False)
    document_number = _sql.Column(_sql.String, index=False)

    partner_account_number = _sql.Column(_sql.String, index=False)
    partner_name = _sql.Column(_sql.String, index=False)
    partner_tax_code = _sql.Column(_sql.String, index=False)
    partner_bank_code = _sql.Column(_sql.String, index=False)

    partner_bank = _sql.Column(_sql.String, index=False)
    tax_payer_code = _sql.Column(_sql.String, index=False)
    tax_payer_name = _sql.Column(_sql.String, index=False)
    payment_id = _sql.Column(_sql.BigInteger, index=True)


class Balance(Base):
    __tablename__ = "balance"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    bank = _sql.Column(_sql.String, index=False)
    account_number = _sql.Column(_sql.String, index=False)
    balance = _sql.Column(_sql.Double, index=False)
    currency = _sql.Column(_sql.String, index=False)
    synced_at_datetime = _sql.Column(_sql.DateTime, default=_dt.datetime.now)
