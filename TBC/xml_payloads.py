TBC_MOVEMENTS_PAYLOAD = {
    "url": "https://secdbi.tbconline.ge/dbi/dbiService",

    "headers": {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': 'http://www.mygemini.com/schemas/mygemini/GetAccountMovements'
    },

    "payload":
        '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:myg="http://www.mygemini.com/schemas/mygemini"
        xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <soapenv:Header>
            <wsse:Security>
                <wsse:UsernameToken>
                    <wsse:Username>{}</wsse:Username>
                    <wsse:Password>{}</wsse:Password>
                    <wsse:Nonce>{}</wsse:Nonce>
                </wsse:UsernameToken>
            </wsse:Security>
        </soapenv:Header>
        <soapenv:Body>
        <myg:GetAccountMovementsRequestIo>
        <myg:accountMovementFilterIo>
        <myg:pager>
        <myg:pageIndex>0</myg:pageIndex>
        <myg:pageSize>100</myg:pageSize>
        </myg:pager>
        <myg:periodFrom>{}</myg:periodFrom>
        <myg:periodTo>{}</myg:periodTo>
        </myg:accountMovementFilterIo>
        </myg:GetAccountMovementsRequestIo>
        </soapenv:Body>
        </soapenv:Envelope>
        '''
}

TBC_ACCOUNT_STATEMENT_PAYLOAD = {
    "url": "https://secdbi.tbconline.ge/dbi/dbiService",

    "headers": {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': 'http://www.mygemini.com/schemas/mygemini/GetAccountStatement'
    },

    "payload":
        '''<?xml version="1.0" encoding="utf-8"?>
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
        xmlns:myg="http://www.mygemini.com/schemas/mygemini" 
        xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
        >
        <soapenv:Header>
        <wsse:Security>
        <wsse:UsernameToken>
        <wsse:Username>{}</wsse:Username>
        <wsse:Password>{}</wsse:Password>
        <wsse:Nonce>{}</wsse:Nonce>
        </wsse:UsernameToken>
        </wsse:Security>
        </soapenv:Header>
        <soapenv:Body>
        <myg:GetAccountStatementRequestIo>
        <myg:filter>
        <myg:periodFrom>2023-04-05</myg:periodFrom>
        <myg:periodTo>{}</myg:periodTo>
        <myg:accountNumber>{}</myg:accountNumber>
        <myg:currency>{}</myg:currency>
        </myg:filter>
        </myg:GetAccountStatementRequestIo>
        </soapenv:Body>
        </soapenv:Envelope>
'''
}

TBC_WITHIN_BANK_PAYMENT_PAYLOAD = {

    "url": "https://secdbi.tbconline.ge/dbi/dbiService",

    "headers": {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': 'http://www.mygemini.com/schemas/mygemini/ImportSinglePaymentOrders'
    },

    "payload":
        '''<?xml version="1.0" encoding="utf-8"?>
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
            xmlns:myg="http://www.mygemini.com/schemas/mygemini" 
            xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            >

            <soapenv:Header>
                <wsse:Security>
                    <wsse:UsernameToken>
                    <wsse:Username>{}</wsse:Username>
                    <wsse:Password>{}</wsse:Password>
                    <wsse:Nonce>{}</wsse:Nonce>
                    </wsse:UsernameToken>
                </wsse:Security>
            </soapenv:Header>
            <soapenv:Body>
            <myg:ImportSinglePaymentOrdersRequestIo>
            <myg:singlePaymentOrder xsi:type="myg:TransferWithinBankPaymentOrderIo">
            <myg:creditAccount>
            <myg:accountNumber>{}</myg:accountNumber>
            </myg:creditAccount>
            <myg:debitAccount>
            <myg:accountNumber>{}</myg:accountNumber>
            <myg:accountCurrencyCode>GEL</myg:accountCurrencyCode>
            </myg:debitAccount>
            <myg:documentNumber>{}</myg:documentNumber>
            <myg:amount>
            <myg:amount>{}</myg:amount>
            <myg:currency>GEL</myg:currency>
            </myg:amount>
            <myg:position>2</myg:position>
            <myg:additionalDescription>{}</myg:additionalDescription>
            <myg:description>{}</myg:description>
            <myg:beneficiaryName>{}</myg:beneficiaryName>
            <myg:beneficiaryTaxCode>{}</myg:beneficiaryTaxCode>
            </myg:singlePaymentOrder>
            </myg:ImportSinglePaymentOrdersRequestIo>    
            </soapenv:Body>
            </soapenv:Envelope>
        '''
}

TBC_OWN_ACC_PAYMENT_PAYLOAD = {

    "url": "https://secdbi.tbconline.ge/dbi/dbiService",

    "headers": {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': 'http://www.mygemini.com/schemas/mygemini/ImportSinglePaymentOrders'
    },

    "payload":
        '''<?xml version="1.0" encoding="utf-8"?>
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
        xmlns:myg="http://www.mygemini.com/schemas/mygemini" 
        xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        >

        <soapenv:Header>
            <wsse:Security>
                <wsse:UsernameToken>
                <wsse:Username>{}</wsse:Username>
                <wsse:Password>{}</wsse:Password>
                <wsse:Nonce>{}</wsse:Nonce>
                </wsse:UsernameToken>
            </wsse:Security>
        </soapenv:Header>
        <soapenv:Body>
        <myg:ImportSinglePaymentOrdersRequestIo>
        <myg:singlePaymentOrder xsi:type="myg:TransferToOwnAccountPaymentOrderIo">

        <myg:creditAccount>
            <myg:accountNumber>{}</myg:accountNumber>
            <myg:accountCurrencyCode>GEL</myg:accountCurrencyCode>
        </myg:creditAccount>

        <myg:debitAccount>
            <myg:accountNumber>{}</myg:accountNumber>
            <myg:accountCurrencyCode>GEL</myg:accountCurrencyCode>
        </myg:debitAccount>

        <myg:documentNumber>{}</myg:documentNumber>

        <myg:amount>
            <myg:amount>{}</myg:amount>
            <myg:currency>GEL</myg:currency>
        </myg:amount>

        <myg:position>3</myg:position>
        <myg:additionalDescription>{}</myg:additionalDescription>
        <myg:description>{}</myg:description>

        </myg:singlePaymentOrder>
        </myg:ImportSinglePaymentOrdersRequestIo>    
        </soapenv:Body>
        </soapenv:Envelope>
        '''
}
