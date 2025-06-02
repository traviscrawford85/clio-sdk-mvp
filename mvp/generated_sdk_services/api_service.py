""" Api SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_api_service import IApiService
from typing import Any

class ApiService(IApiService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

