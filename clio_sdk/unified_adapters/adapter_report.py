from clio_client.models import Report as ClioReport
from clio_sdk.adapter_factory.base import make_model_adapter
from clio_sdk.unified_models.report import Report as DomainReport

adapter = make_model_adapter(ClioReport, DomainReport, name="report")
