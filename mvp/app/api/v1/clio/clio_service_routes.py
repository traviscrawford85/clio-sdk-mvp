# app/api/v1/clio_service_routes.py

from fastapi import APIRouter, Depends, HTTPException
from clio_sdk_mvp.clio_sdk.services.statute_service import StatuteService as ClioStatuteOfLimitationsService
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK 
from app.api.v1.schemas import UpdateStatuteResponse

router = APIRouter()

def get_clio_statute_service() -> ClioStatuteOfLimitationsService:
    api_client = get_clio_api_client()
    return ClioStatuteOfLimitationsService(api_client)

@router.post(
    "/clio/update_statute_of_limitations_auto",
    response_model=UpdateStatuteResponse
)
async def update_statute_of_limitations_auto(
    matter_id: int,
    sol_service: ClioStatuteOfLimitationsService = Depends(get_clio_statute_service),
):
    try:
        result = sol_service.update_statute_of_limitations(matter_id)
        return result  # ✅ Let FastAPI handle serialization
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
