"""
Database models.
"""
from django.db import models

class Task(models.Model):
    """
    Task model class.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
