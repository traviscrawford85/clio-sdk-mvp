""" Payments SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_payments_service import IPaymentsService
from typing import Any

class PaymentsService(IPaymentsService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

