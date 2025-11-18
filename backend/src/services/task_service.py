from typing import List, Dict, Any
from datetime import datetime, timedelta
from loguru import logger
from mongoengine import DoesNotExist, ValidationError

from src.models import TaskModel


class TaskService:
    
    def _serialize_task(self, task):
        data = task.to_mongo().to_dict()
        data["id"] = str(data.pop("_id"))
        return data
    
    def get_all_tasks(self, filter: str = "today") -> List[Dict[str, Any]]:
        
        now = datetime.now()
        start_date = None

        if filter == "today":
            start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
        elif filter == "week":
            start_date = (now - timedelta(days=now.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
        elif filter == "month":
            start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        elif filter == "all":
            start_date = None
            
        match_stage = {}
        if start_date:
            match_stage["created_at"] = {"$gte": start_date}
        
        try:
            pipeline = [
                {"$match": match_stage},
                {
                    "$facet": {
                        "tasks": [
                            {"$sort": {"created_at": -1}}
                        ],
                        "active_count": [
                            {"$match": {"status": "active"}},
                            {"$count": "count"}
                        ],
                        "complete_count": [
                            {"$match": {"status": "complete"}},
                            {"$count": "count"}
                        ]
                    }
                }
            ]
            result = list(TaskModel.objects.aggregate(*pipeline))[0]
            tasks = result["tasks"]
            for task in tasks:
                task["id"] = str(task.pop("_id"))
            active_count = result["active_count"][0]["count"] if len(result["active_count"]) > 0 else 0
            complete_count = result["complete_count"][0]["count"] if len(result["complete_count"]) > 0 else 0
            return {
                "tasks": tasks,
                "active_count": active_count,
                "complete_count": complete_count
            }
        except Exception as e:
            logger.error(f"Failed to fetch tasks: {e}")
            raise

    def get_task_by_id(self, task_id: str) -> Dict[str, Any]:
        try: 
            task = TaskModel.objects.get(id=task_id)
            return self._serialize_task(task)
        except DoesNotExist as e:
            logger.error(f"Task {task_id} not found")
            raise
        except Exception as e:
            logger.error(f"Failed to fetch task: {e}")
            raise

    def create_task(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            task = TaskModel(**data)
            task.save()
            return self._serialize_task(task)
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            raise
        except Exception as e:
            logger.error(f"Failed to create task: {e}")
            raise

    def update_task(self, task_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            task = TaskModel.objects.get(id=task_id)
            for key, value in data.items():
                if value is not None:
                    setattr(task, key, value)
            task.save()
            return self._serialize_task(task)
        except DoesNotExist:
            logger.error(f"Task {task_id} not found")
            raise
        except Exception as e:
            logger.error(f"Failed to update task {task_id}: {e}")
            raise

    def delete_task(self, task_id: str) -> Dict[str, Any]:
        try:
            task = TaskModel.objects.get(id=task_id)
            task.delete()
            return {"message": f"Task {task_id} deleted successfully"}
        except DoesNotExist:
            logger.error(f"Task {task_id} not found")
            raise
        except Exception as e:
            logger.error(f"Failed to delete task {task_id}: {e}")
            raise