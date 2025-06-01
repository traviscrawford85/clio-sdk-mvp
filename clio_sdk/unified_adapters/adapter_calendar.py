from clio_client.models import Calendar as ClioCalendar
from clio_sdk.adapter_factory.base import make_model_adapter
from clio_sdk.unified_models.calendar import Calendar as DomainCalendar

adapter = make_model_adapter(ClioCalendar, DomainCalendar, name="calendar")
