""" Communications SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_communications_service import ICommunicationsService
from typing import Any

class CommunicationsService(ICommunicationsService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

