"""
Unified ClioSDK class that aggregates all tag group modules for discoverable, ergonomic API access.
"""
from clio_sdk.api_modules import (
    activity,
    calendar,
    client,
    contact,
    custom_field,
    custom_field_value,
    document,
    matter,
    note,
    report,
    statute,
    task,
    user,
    webhook
)

from typing import Any


class ClioSDK:
    def __init__(self, **client_kwargs: Any):
        self.activity = activity
        self.calendar = calendar
        self.client = client
        self.contact = contact
        self.custom_field = custom_field
        self.custom_field_value = custom_field_value
        self.document = document
        self.matter = matter
        self.note = note
        self.report = report
        self.statute = statute
        self.task = task
        self.user = user
        self.webhook = webhook
        self._client_kwargs = client_kwargs
