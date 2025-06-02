# app/api/v1/qbo_routes.py

from fastapi import APIRouter, Depends
from app.auth.jwt_auth import auth_wrapper
from app.services import qbo_service
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
router = APIRouter()

@router.get("/qbo/payments")
async def get_payments(limit: int = 10, token_data=Depends(auth_wrapper)):
    """Fetch recent payments from QuickBooks."""
    payments = qbo_service.fetch_recent_payments(limit=limit)
    return {"payments": [payment.to_dict() for payment in payments]}

@router.get("/qbo/customers")
async def get_customers(limit: int = 10, token_data=Depends(auth_wrapper)):
    """Fetch recent customers from QuickBooks."""
    customers = qbo_service.fetch_customers(limit=limit)
    return {"customers": [customer.to_dict() for customer in customers]}

@router.get("/qbo/vendors")
async def get_vendors(limit: int = 10, token_data=Depends(auth_wrapper)):
    """Fetch recent vendors from QuickBooks."""
    vendors = qbo_service.fetch_vendors(limit=limit)
    return {"vendors": [vendor.to_dict() for vendor in vendors]}
