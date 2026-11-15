from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_user, login_user, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('auth/register/', register_user, name='register'),
    path('auth/login/', login_user, name='login'),
    path('', include(router.urls)),
]