# clio/api/routes/matters_router.py

from fastapi import APIRouter, HTTPException, status

from clio.api.models.MatterUpdateInputModel import MatterUpdateInputModel
from clio.api.models.MatterViewModel import MatterViewModel
from clio.matters import get_matter_by_id
from clio_client.exceptions import UnauthorizedException
from clio_sdk.builders.matter_request_builder import build_full_update_request
from clio_sdk.client import ClioClient
from clio_sdk.services.matter_service import update_matter_custom_field

router = APIRouter(prefix="/matters", tags=["Matters"])


@router.get("/{matter_id}", response_model=MatterViewModel)
async def read_matter(matter_id: int):
    """
    Retrieves matter details by ID.
    """
    try:
        matter = get_matter_by_id(matter_id)
        if not matter:
            raise HTTPException(status_code=404, detail="Matter not found")
        return matter
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{matter_id}", response_model=MatterViewModel)
async def update_matter(matter_id: int, update_data: MatterUpdateInputModel):
    """
    Updates a matter's metadata such as status, close_date, custom fields, etc.
    """
    try:
        return update_matter_custom_field(matter_id, update_data)
    except UnauthorizedException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized: Invalid or expired token."
        )
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Failed to update matter: {str(e)}"
        )
