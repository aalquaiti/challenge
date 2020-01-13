from django.urls import path, include
from rest_framework.routers import DefaultRouter
from control import views

router = DefaultRouter()
router.register('control', views.ControlViewSet)

urlpatterns = [
    # path('control/upload/', views.ControlUploadView),
    path('', include(router.urls)),
]