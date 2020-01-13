# Created by: Aymen Al-Quaiti
# For QCTRL Backend Challenge
# January  2020
"""
Includes URLs and routes handled by the app. Root path for the app is defined under the project folder qctrl/urls.py
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ControlViewSet

# Create router and added its generated URLS to path
router = DefaultRouter()
router.register('control', ControlViewSet)
# router.register('download', ControlCSVViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
