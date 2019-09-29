from transbank.common.model import CardDetail


class TransactionCreateResponse(object):
    def __init__(self, token: str):
        self.token = token

    def __repr__(self):
        return "token: {}".format(self.token)


class TransactionCommitResponse(object):
    def __init__(self,
                 # vci: str,
                 amount: float, status: str, buy_order: str, session_id: str,
                 card_detail: CardDetail, accounting_date: str, transaction_date: str, authorization_code: str,
                 payment_type_code: str, response_code: str, installments_number: float,
                 # installments_amount: float,
                 # balance: float
                 ):
        # self.vci = vci
        self.amount = amount
        self.status = status
        self.buy_order = buy_order
        self.session_id = session_id
        self.card_detail = card_detail
        self.accounting_date = accounting_date
        self.transaction_date = transaction_date
        self.authorization_code = authorization_code
        self.payment_type_code = payment_type_code
        self.response_code = response_code
        self.installments_number = installments_number
        # self.installments_amount = installments_amount
        # self.balance = balance


class TransactionStatusResponse(object):
    def __init__(self, vci: str, amount: float, status: str, buy_order: str, session_id: str,
                 card_detail: CardDetail, accounting_date: str, transaction_date: str, authorization_code: str,
                 payment_type_code: str, response_code: str, installments_number: float, installments_amount: float,
                 balance: float):
        self.vci = vci
        self.amount = amount
        self.status = status
        self.buy_order = buy_order
        self.session_id = session_id
        self.card_detail = card_detail
        self.accounting_date = accounting_date
        self.transaction_date = transaction_date
        self.authorization_code = authorization_code
        self.payment_type_code = payment_type_code
        self.response_code = response_code
        self.installments_number = installments_number
        self.installments_amount = installments_amount
        self.balance = balance

    def __repr__(self):
        return """
        vci: {},
        amount: {},
        status: {},
        buy_order: {},
        session_id: {},
        card_detail: {},
        accounting_date: {},
        transaction_date: {},
        authorization_code: {},
        payment_type_code: {},
        response_code: {},
        installments_number: {},
        installments_amount: {},
        balance:{}
        """.format(self.vci, self.amount, self.status, self.buy_order, self.session_id, self.card_detail,
                   self.card_detail,
                   self.accounting_date, self.transaction_date, self.authorization_code, self.payment_type_code,
                   self.response_code, self.installments_number, self.installments_amount, self.balance)


class TransactionRefundResponse(object):
    def __init__(self, type: str, authorization_code: str, authorization_date: str, nullified_amount: float,
                 balance: float, response_code: str):
        self.type = type
        self.authorization_code = authorization_code
        self.authorization_date = authorization_date
        self.nullified_amount = nullified_amount
        self.balance = balance
        self.response_code = response_code

    def __repr__(self):
        return """
        type: {},
        authorization_code: {},
        authorization_date: {},
        nullified_amount: {},
        balance: {},
        response_code: {}
        """.format(self.type, self.authorization_code, self.authorization_date, self.nullified_amount, self.balance,
                   self.response_code)


class TransactionInstallmentsResponse(object):
    def __init__(self, installments_amount: float, id_query_installments: str, deferred_periods: str):
        self.installments_amount = installments_amount
        self.id_query_installments = id_query_installments
        self.deferred_periods = deferred_periods

    def __repr__(self):
        return """
        installments_amount: {},
        id_query_installments: {},
        deferred_periods: {}
        """.format(self.installments_amount, self.id_query_installments, self.deferred_periods)


class TransactionStatusResponse(object):
    def __init__(self,
                 amount: float, status: str, buy_order: str, session_id: str,
                 card_detail: CardDetail, accounting_date: str, transaction_date: str, authorization_code: str,
                 payment_type_code: str, response_code: str, installments_number: float,
                 ):
        self.amount = amount
        self.status = status
        self.buy_order = buy_order
        self.session_id = session_id
        self.card_detail = card_detail
        self.accounting_date = accounting_date
        self.transaction_date = transaction_date
        self.authorization_code = authorization_code
        self.payment_type_code = payment_type_code
        self.response_code = response_code
        self.installments_number = installments_number

    def __repr__(self):
        return """
        amount: {},
        status: {},
        buy_order: {},
        session_id: {},
        card_detail: {},
        accounting_date: {},
        transaction_date: {},
        authorization_code: {},
        payment_type_code: {},
        response_code: {},
        installments_number: {},
        """.format(self.amount, self.status, self.buy_order, self.session_id, self.card_detail,
                   self.card_detail,
                   self.accounting_date, self.transaction_date, self.authorization_code, self.payment_type_code,
                   self.response_code, self.installments_number)