"""
Views for manage the task APIs.
"""

from rest_framework import viewsets

from core.models import Task
from task.serializers import CreateTaskSerializers, UpdateTaskSerializers

class TaskViewSet(viewsets.ModelViewSet):
    """
    Manage task in the database.
    """
    serializer_class = CreateTaskSerializers
    queryset = Task.objects.all()
    
    def get_serializer_class(self):
        """
        Return the serializer class for request.
        """
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return UpdateTaskSerializers
        else:
            return CreateTaskSerializers
