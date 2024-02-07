from django.db import models


class Todo(models.Model):
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
