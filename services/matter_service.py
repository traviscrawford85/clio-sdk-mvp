# MatterService that implements the IMatterService interface
from typing import List, Optional

from clio.token_store import get_access_token
from clio_client.api.matters_api import MattersApi
from clio_client.api_client import ApiClient
from clio_client.configuration import Configuration
from clio_sdk.adapter_factory import get_adapter
from clio_sdk.client.client import ClioClient
from clio_sdk.commands.matter_commands import build_full_update_request
from clio_sdk.interfaces.i_matter_service import IMatterService
from clio_sdk.unified_models.matter import (
    Matter,
    MatterUpdateInputModel,
    ResponsibleStaffModel,
)


def get_api_client() -> MattersApi:
    config = Configuration()
    token = get_access_token()
    config.access_token = token
    return MattersApi(ApiClient(config))


class MatterService(IMatterService):
    def __init__(self, client: ClioClient):
        self.client = client
        self.adapter = get_adapter("matter")


def get_matter(self, matter_id: int) -> Optional[Matter]:
    """
    @service-interface: IMatterService
    @return: Unknown
    @args: matter_id: int
    """
    resp = self.client.get_matter(matter_id)
    if resp.status_code == 200 and resp.parsed:
        return self.adapter["from_clio"](resp.parsed.matter)
    return None

    def update_matter(self, matter_id: int, update: MatterUpdateInputModel) -> bool:
        """
        @service-interface: IMatterService
        @return: Unknown
        @args: matter_id: int, update: MatterUpdateInputModel
        """
        req = build_full_update_request(update)
        resp = self.client.update_matter(matter_id, req)
        return resp.status_code == 200

    """
    @service-interface: IMatterService
    @return: Unknown
    @args: 
    """

    def list_matters(self) -> List[Matter]:
        resp = self.client.list_matters()
        if resp.status_code == 200 and resp.parsed:
            return [self.adapter["from_clio"](m) for m in resp.parsed.matters]
        return []

    """
    @service-interface: IMatterService
    @return: Unknown
    @args: matter_id: int
    """

    def get_blank_custom_fields(self, matter_id: int) -> List[dict]:
        matter = self.get_matter(matter_id)
        if not matter or not getattr(matter, "custom_field_values", None):
            return []
        return [cf for cf in matter.custom_field_values if not cf.value]

    """
    @service-interface: IMatterService
    @return: Unknown
    @args: matter_id: int
    """

    def delete_blank_custom_fields(self, matter_id: int) -> bool:
        blank_fields = self.get_blank_custom_fields(matter_id)
        for cf in blank_fields:
            self.client.update_custom_field(matter_id, cf.id, {"_destroy": True})
        return True

    """
    @service-interface: IMatterService
    @return: Unknown
    @args: matter_ids: List[int], status: str
    """

    def batch_update_status(self, matter_ids: List[int], status: str) -> List[bool]:
        return [
            self.update_matter(mid, MatterUpdateInputModel(status=status))
            for mid in matter_ids
        ]

    """
    @service-interface: IMatterService
    @return: Unknown
    @args: 
    """

    def batch_update_responsible_staff(
        self, matter_ids: List[int], user_id: int
    ) -> List[bool]:
        return [
            self.update_matter(
                mid,
                MatterUpdateInputModel(
                    responsible_staff=ResponsibleStaffModel(id=user_id)
                ),
            )
            for mid in matter_ids
        ]
