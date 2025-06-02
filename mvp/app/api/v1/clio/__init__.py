from fastapi import APIRouter
from .routes import router as base_clio_router
from .clio_service_routes import router as clio_service_router

router = APIRouter()
router.include_router(base_clio_router)
router.include_router(clio_service_router)
