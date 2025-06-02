""" Reporting SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_reporting_service import IReportingService
from typing import Any

class ReportingService(IReportingService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

