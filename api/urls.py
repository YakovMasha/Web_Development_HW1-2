from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, OrganizationViewSet

# Создаём роутер
router = SimpleRouter()

# Регистрируем ViewSets
router.register(r'user', UserViewSet)
router.register(r'organization', OrganizationViewSet)

# Основные URL-паттерны
urlpatterns = [
    path('', include(router.urls)),
]