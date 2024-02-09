from django.db import models
from account.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    status = models.IntegerField(default=0, choices=(
        (0, 'In Progress'),
        (1, 'Completed'),
        (2, 'Deleted')
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
