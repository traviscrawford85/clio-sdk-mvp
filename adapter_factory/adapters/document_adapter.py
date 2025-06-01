from clio_client.models.document import ClioDocument
from clio_sdk.models.document import Document
from clio_sdk.adapter_factory.base import make_model_adapter

adapter = make_model_adapter(ClioDocument, Document, name="document")