from clio_client.models.report import ClioReport
from clio_sdk.models.report import Report
from clio_sdk.adapter_factory.base import make_model_adapter

adapter = make_model_adapter(ClioReport, Report, name="report")