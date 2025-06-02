""" Contacts SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_contacts_service import IContactsService
from typing import Any

class ContactsService(IContactsService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

