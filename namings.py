TBC_MOVEMENT_API_FIELD_NAMINGS = {
    "ns2:movementId": "movement_id",
    "ns2:externalPaymentId": "external_payment_id",  # API unique identifier
    "ns2:debitCredit": "debit_credit",
    "ns2:documentDate": "document_date",
    "ns2:description": "description",
    "ns2:amount": "amount",
    "ns2:currency": "currency",
    "ns2:accountNumber": "sc_account_number",
    "ns2:accountName": "sc_account_name",
    "ns2:additionalInformation": "additional_info",
    "ns2:documentNumber": "document_number",
    "ns2:partnerAccountNumber": "partner_account_number",
    "ns2:partnerName": "partner_name",
    "ns2:partnerTaxCode": "partner_tax_code",
    "ns2:partnerBankCode": "partner_bank_code",
    "ns2:partnerBank": "partner_bank",
    "ns2:taxpayerCode": "tax_payer_code",
    "ns2:taxpayerName": "tax_payer_name",
    "ns2:paymentId": "payment_id",
}

ACCOUNTS_DATA = {
    "GE01TB1234567891234567": "ACCOUNT_OWNER_USERNAME",
    "GE02TB1234567891234567": "ACCOUNT_OWNER_USERNAME",
    "GE03TB1234567891234567": "ACCOUNT_OWNER_USERNAME",
    "GE04TB1234567891234567": "ACCOUNT_OWNER_USERNAME"
}

STATUS_CODES = {
    "WC": {
        "geo": "ავტორიზაციის მოლოდინში",
        "en": "Waiting for certificate",
    },

    "CERT": {
        "geo": "დამუშავების პროცესში",
        "en": "In Progress",
    },

    "VERIF": {
        "geo": "დამუშავების პროცესში",
        "en": "In Progress",
    },
    "WS": {
        "geo": "დამუშავების პროცესში",
        "en": "In Progress",
    },

    "F": {
        "geo": "დასრულებული",
        "en": "Finished Successfully",
    },

    "FL": {
        "geo": "უარყოფილი",
        "en": "Failed",
    },

    "C": {
        "geo": "გაუქმებული",
        "en": "Cancelled",
    },
}

NESTED_XML_TAGS = [
    "amount",
]
