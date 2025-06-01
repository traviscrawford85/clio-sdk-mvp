from typing import Optional

from clio_client.models import Report as ClioReport
from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.report import Report as DomainReport


def transform_report_fields(data: dict, context: Optional[dict] = None) -> dict:
    # TODO: Add field mapping logic here
    return data

register_transformer("report", transform_report_fields)
