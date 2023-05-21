"""
Serializer for Task APIs.
"""

from rest_framework import serializers
from core.models import Task

class CreateTaskSerializers(serializers.ModelSerializer):
    """
    Serializer for creating a task.
    """
    
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'is_finished', 'created']
        ordering = ['is_finished', 'created']

class UpdateTaskSerializers(serializers.ModelSerializer):
    """
    Serializer for Updating a task.
    """
    
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'created']
        ordering = ['is_finished', 'created']
