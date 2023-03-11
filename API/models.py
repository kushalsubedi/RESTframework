from django.db import models
import uuid
# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField (primary_key=True, default=uuid.uuid4, editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Todo(BaseModel):
    
    title=models.CharField(max_length=255)
    description=models.TextField()
    completed=models.BooleanField(default=False)
    due_date=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title