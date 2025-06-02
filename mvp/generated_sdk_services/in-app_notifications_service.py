""" In-app Notifications SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_in-app_notifications_service import IIn-appNotificationsService
from typing import Any

class In-appNotificationsService(IIn-appNotificationsService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

