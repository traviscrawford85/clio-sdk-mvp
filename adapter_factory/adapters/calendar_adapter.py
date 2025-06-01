from clio_client.models.calendar import ClioCalendar
from clio_sdk.models.calendar import Calendar
from clio_sdk.adapter_factory.base import make_model_adapter

adapter = make_model_adapter(ClioCalendar, Calendar, name="calendar")