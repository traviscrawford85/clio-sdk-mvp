""" Accounting SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_accounting_service import IAccountingService
from typing import Any

class AccountingService(IAccountingService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

