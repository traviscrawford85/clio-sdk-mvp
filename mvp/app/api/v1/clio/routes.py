# app/api/v1/clio/routes.py

from fastapi import APIRouter, Depends
from dotenv import load_dotenv
from datetime import datetime

from app.auth.jwt_auth import auth_wrapper
from clio_sdk_mvp.clio_sdk.services.task_service import TaskService as ClioTaskService
from clio_sdk_mvp.clio_sdk.services.custom_field_service import CustomFieldService as ClioCustomFieldService
from clio_sdk_mvp.clio_sdk.services.statute_service import StatuteService
from app.celery_tasks.task_workers import process_task
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK

load_dotenv()

router = APIRouter()

# --- Dependency Functions ---
def get_clio_sdk():
    # You may want to inject the access token from your token store here
    from app.core.token_store import get_access_token
    return ClioSDK(access_token=get_access_token())

# --- Service Dependency Functions ---
def get_clio_task_service() -> ClioTaskService:
    return ClioTaskService(get_clio_sdk())

def get_clio_custom_field_service() -> ClioCustomFieldService:
    return ClioCustomFieldService(get_clio_sdk())

def get_clio_statute_service() -> StatuteService:
    return StatuteService(get_clio_sdk())


# --- Task Assignment & Processing Routes ---

@router.post("/clio/assign_task")
async def assign_task(
    task_id: int,
    worker_id: str,
    token_data=Depends(auth_wrapper),
    task_service: ClioTaskService = Depends(get_clio_task_service),
):
    """Assign a task to a worker."""
    task = task_service.assign_task_to_worker(task_id, worker_id)
    return {
        "status": "assigned",
        "task_id": task.id,
        "worker_id": worker_id,
        "task_status": task.status,
    }

@router.post("/clio/start_task_processing")
async def start_task_processing(
    task_id: int,
    worker_id: str,
    token_data=Depends(auth_wrapper),
):
    """Trigger background task processing."""
    process_task.delay(task_id, worker_id)
    return {
        "status": "processing started",
        "task_id": task_id,
        "worker_id": worker_id,
    }

# --- Custom Field Utility Routes ---

@router.post("/clio/compute_statute_of_limitations")
async def compute_statute_of_limitations(
    matter_id: int,
    token_data=Depends(auth_wrapper),
    custom_service: ClioCustomFieldService = Depends(get_clio_custom_field_service),
):
    """Compute and store the Statute of Limitations based on Incident Date."""
    incident_date = custom_service.get_date_of_incident(matter_id)
    statute_date = incident_date.replace(year=incident_date.year + 2)
    custom_service.set_statute_of_limitations(matter_id, statute_date)

    return {
        "status": "computed",
        "matter_id": matter_id,
        "incident_date": incident_date.strftime("%Y-%m-%d"),
        "statute_of_limitations_date": statute_date.strftime("%Y-%m-%d"),
    }

@router.post("/clio/test_set_statute_of_limitations")
async def test_set_statute_of_limitations(
    matter_id: int,
    due_date: str,
    token_data=Depends(auth_wrapper),
    custom_service: ClioCustomFieldService = Depends(get_clio_custom_field_service),
):
    """Manually set a Statute of Limitations date for a Matter (testing)."""
    statute_date = datetime.strptime(due_date, "%Y-%m-%d")
    custom_service.set_statute_of_limitations(matter_id, statute_date)

    return {
        "status": "updated manually",
        "matter_id": matter_id,
        "due_date": due_date
    }

# --- Full Auto-Compute and Patch Statute of Limitations Routes ---

@router.post("/clio/test_update_sol")
async def test_update_statute_of_limitations(matter_id: int):
    """(Old) Manual way to test SOL update via direct instantiation."""
    sol_service = StatuteService(get_clio_sdk())
    result = sol_service.update_statute_of_limitations(matter_id)
    return result

@router.post("/clio/update_statute_of_limitations_auto")
async def update_statute_of_limitations_auto(
    matter_id: int,
    token_data=Depends(auth_wrapper),
    sol_service: StatuteService = Depends(get_clio_statute_service),
):
    """Auto-compute and PATCH Statute of Limitations via Clio OpenAPI Client."""
    result = sol_service.update_statute_of_limitations(matter_id)
    return result
