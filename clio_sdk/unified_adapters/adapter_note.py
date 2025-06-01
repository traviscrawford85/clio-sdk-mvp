from clio_client.models import Note as ClioNote
from clio_sdk.adapter_factory.base import make_model_adapter
from clio_sdk.unified_models.note import Note as DomainNote

adapter = make_model_adapter(ClioNote, DomainNote, name="note")
