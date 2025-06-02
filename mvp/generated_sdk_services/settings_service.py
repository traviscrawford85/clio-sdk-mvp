""" Settings SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_settings_service import ISettingsService
from typing import Any

class SettingsService(ISettingsService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

