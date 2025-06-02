""" Documents SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_documents_service import IDocumentsService
from typing import Any

class DocumentsService(IDocumentsService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

