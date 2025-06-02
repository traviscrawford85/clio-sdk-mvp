""" Legal Aid England & Wales SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_legal_aid_england_&_wales_service import ILegalAidEngland&WalesService
from typing import Any

class LegalAidEngland&WalesService(ILegalAidEngland&WalesService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

