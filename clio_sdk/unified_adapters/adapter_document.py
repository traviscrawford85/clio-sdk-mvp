from clio_client.models import Document as ClioDocument
from clio_sdk.adapter_factory.base import make_model_adapter
from clio_sdk.unified_models.document import Document as DomainDocument

adapter = make_model_adapter(ClioDocument, DomainDocument, name="document")
