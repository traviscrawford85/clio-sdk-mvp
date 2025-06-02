""" Trust SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_trust_service import ITrustService
from typing import Any

class TrustService(ITrustService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

