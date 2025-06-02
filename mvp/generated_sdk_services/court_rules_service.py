""" Court Rules SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_court_rules_service import ICourtRulesService
from typing import Any

class CourtRulesService(ICourtRulesService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

