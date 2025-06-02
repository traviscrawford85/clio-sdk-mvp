""" Users SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_users_service import IUsersService
from typing import Any

class UsersService(IUsersService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

