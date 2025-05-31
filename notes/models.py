from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=255)
    note = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='notes', null=True)  # Many-to-One
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp created
    updated_at = models.DateTimeField(auto_now=True)      # timestamp updated
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
