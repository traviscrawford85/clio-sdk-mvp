""" Billing SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_billing_service import IBillingService
from typing import Any

class BillingService(IBillingService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

