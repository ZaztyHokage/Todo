from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = None

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


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
