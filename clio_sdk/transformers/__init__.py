from .activity_transformer import transform_activity_fields
from .calendar_transformer import transform_calendar_fields
from .client_transformer import transform_client_fields
from .contact_transformer import transform_contact_fields
from .custom_field_transformer import transform_custom_field_fields
from .custom_field_value_transformer import transform_custom_field_value_fields
from .document_transformer import transform_document_fields
from .matter_transformer import transform_matter_fields
from .note_transformer import transform_note_fields
from .report_transformer import transform_report_fields
from .task_transformer import transform_task_fields
from .user_transformer import transform_user_fields
from .webhook_transformer import transform_webhook_fields

transformer_registry = {
    "contact": transform_contact_fields,
    "matter": transform_matter_fields,
    "task": transform_task_fields,
    "webhook": transform_webhook_fields,
    "client": transform_client_fields,
    "calendar": transform_calendar_fields,
    "activity": transform_activity_fields,
    "document": transform_document_fields,
    "note": transform_note_fields,
    "custom_field": transform_custom_field_fields,
    "custom_field_value": transform_custom_field_value_fields,
    "user": transform_user_fields,
    "report": transform_report_fields,
}


def get_transformer(name: str):
    return transformer_registry.get(name)
