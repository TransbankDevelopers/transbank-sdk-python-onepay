import requests
from transbank.error.transaction_commit_error import TransactionCommitError

from transbank.error.transaction_create_error import TransactionCreateError

from transbank.common.headers_builder import HeadersBuilder
from transbank.common.integration_type import IntegrationType, webpay_host
from transbank.common.options import Options, WebpayOptions
from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.webpay.webpay_plus.request import TransactionCreateRequest, TransactionRefundRequest
from transbank.webpay.webpay_plus.response import TransactionCreateResponse, TransactionCommitResponse, \
    TransactionRefundResponse, TransactionStatusResponse
from transbank.webpay.webpay_plus.schema import TransactionStatusResponseSchema, TransactionCreateRequestSchema, \
    TransactionCreateResponseSchema, TransactionCommitResponseSchema, TransactionRefundRequestSchema, \
    TransactionRefundResponseSchema
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.webpay.webpay_plus import webpay_plus_deferred_commerce_code, default_api_key, default_integration_type


class DeferredTransaction(object):
    @classmethod
    def __base_url(cls, integration_type: IntegrationType) -> str:
        return "{}/rswebpaytransaction/api/webpay/v1.0/transactions".format(
            webpay_host(integration_type))

    @classmethod
    def build_options(cls, options: Options = None) -> Options:
        alt_options = WebpayOptions(webpay_plus_deferred_commerce_code, default_api_key, default_integration_type)

        if options is not None:
            alt_options.commerce_code = options.commerce_code or webpay_plus_deferred_commerce_code
            alt_options.api_key = options.api_key or default_api_key
            alt_options.integration_type = options.integration_type or default_integration_type

        return alt_options

    @classmethod
    def create(cls, buy_order: str, session_id: str, amount: float, return_url: str, options: Options = None) \
            -> TransactionCreateResponse:
        options = cls.build_options(options)
        endpoint = cls.__base_url(options.integration_type)
        request = TransactionCreateRequest(buy_order, session_id, amount, return_url)

        response = requests.post(endpoint, data=TransactionCreateRequestSchema().dumps(request).data,
                                 headers=HeadersBuilder.build(options))
        json_response = response.text
        dict_response = TransactionCreateResponseSchema().loads(json_response).data

        if response.status_code not in (200, 299):
            raise TransactionCreateError(message=dict_response["error_message"], code=response.status_code)

        return TransactionCreateResponse(**dict_response)