from mongoengine import Document, StringField, DateTimeField

from src.utils import get_current_time


class TaskModel(Document):
    title = StringField(required=True)
    status = StringField(choices=["active", "complete"], default="active")
    completed_at = DateTimeField(default=None)
    created_at = DateTimeField(default=get_current_time)
    updated_at = DateTimeField(default=get_current_time)
    
    meta = {
        "collection": "tasks"
    }
    
    def save(self, *args, **kwargs):
        self.updated_at = get_current_time()
        return super().save(*args, **kwargs)