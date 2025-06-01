# adapter_factory/transformers/matter_transformer.py

from typing import Any, Dict, List, Optional


class MatterTransformer:
    @staticmethod
    def transform_task(task: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "id": task.get("id"),
            "name": task.get("name"),
            "status": task.get("status", "pending").lower(),
            "due_date": task.get("due_date"),
            "created_at": task.get("created_at"),
            "updated_at": task.get("updated_at"),
        }

    @staticmethod
    def from_clio(
        data: Dict[str, Any], context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        client = data.get("client", {})
        currency = data.get("currency", {})
        custom_rate = data.get("custom_rate", {})
        responsible_attorney = data.get("responsible_attorney", {})
        matter_stage = data.get("matter_stage", {})
        tasks_data = data.get("tasks", [])

        transformed_tasks = [
            MatterTransformer.transform_task(task) for task in tasks_data
        ]

        if context is not None:
            context.setdefault("tasks", []).extend(transformed_tasks)

        return {
            "id": data.get("id"),
            "description": data.get("description"),
            "status": data.get("status", "pending").lower(),
            "client": {
                "id": client.get("id"),
                "name": client.get("name"),
                "email": client.get("primary_email_address"),
                "phone": client.get("primary_phone_number"),
            },
            "currency_code": currency.get("code"),
            "custom_rate_type": custom_rate.get("type"),
            "responsible_attorney": {
                "id": responsible_attorney.get("id"),
                "name": responsible_attorney.get("name"),
                "email": responsible_attorney.get("email"),
            },
            "matter_stage": {
                "id": matter_stage.get("id"),
                "name": matter_stage.get("name"),
            },
            "created_at": data.get("created_at"),
            "updated_at": data.get("updated_at"),
        }
