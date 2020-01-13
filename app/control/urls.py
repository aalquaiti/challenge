from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ControlViewSet, ControlCSVViewSet

router = DefaultRouter()
router.register('control', ControlViewSet)
router.register('download', ControlCSVViewSet)

urlpatterns = [
    path('', include(router.urls)),
]