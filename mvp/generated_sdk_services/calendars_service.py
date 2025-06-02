""" Calendars SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_calendars_service import ICalendarsService
from typing import Any

class CalendarsService(ICalendarsService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

