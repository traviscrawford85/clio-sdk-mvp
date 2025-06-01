from clio_client.models.note import ClioNote
from clio_sdk.models.note import Note
from clio_sdk.adapter_factory.base import make_model_adapter

adapter = make_model_adapter(ClioNote, Note, name="note")