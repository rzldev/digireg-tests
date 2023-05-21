"""
URL mappings for task APIs.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task import views

app_name = 'task'

router = DefaultRouter()
router.register('task', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]