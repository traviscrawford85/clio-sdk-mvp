""" Clio Payments SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_clio_payments_service import IClioPaymentsService
from typing import Any

class ClioPaymentsService(IClioPaymentsService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

