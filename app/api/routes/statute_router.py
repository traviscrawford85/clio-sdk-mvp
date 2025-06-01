# clio/api/routes/statute_router.py
import logging

from fastapi import APIRouter, HTTPException

from clio_sdk.services.statute_service import compute_statute_for_matter
from clio_sdk.services.statute_sync_api_service import sync_statute_to_matter

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/statuteoflimitations", tags=["Statute of Limitations"])

@router.get("/compute/{matter_id}")
async def compute_statute(matter_id: int):
    logger.info(f"Received request to compute statute for matter {matter_id}")
    try:
        date = await compute_statute_for_matter(matter_id)
        logger.info(f"Computed statute of limitations for matter {matter_id}: {date}")
        return {"computed_statute_of_limitations": date}
    except HTTPException as e:
        logger.error(f"HTTPException while computing statute for matter {matter_id}: {e.detail}")
        raise e
    except Exception as e:
        logger.exception(f"Unexpected error while computing statute for matter {matter_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/sync/{matter_id}")
async def sync_statute(matter_id: int):
    logger.info(f"Received request to sync statute for matter {matter_id}")
    try:
        await sync_statute_to_matter(matter_id)
        logger.info(f"Successfully synced statute of limitations for matter {matter_id}")
        return {"message": "Statute of limitations synced successfully."}
    except HTTPException as e:
        logger.error(f"HTTPException while syncing statute for matter {matter_id}: {e.detail}")
        raise e
    except Exception as e:
        logger.exception(f"Unexpected error while syncing statute for matter {matter_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
