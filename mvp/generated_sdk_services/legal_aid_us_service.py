""" Legal Aid US SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_legal_aid_us_service import ILegalAidUSService
from typing import Any

class LegalAidUSService(ILegalAidUSService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

