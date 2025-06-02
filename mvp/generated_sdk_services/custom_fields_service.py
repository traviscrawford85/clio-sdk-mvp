""" Custom Fields SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_custom_fields_service import ICustomFieldsService
from typing import Any

class CustomFieldsService(ICustomFieldsService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

