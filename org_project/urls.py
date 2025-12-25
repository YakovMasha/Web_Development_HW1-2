from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('', include('orgapp.urls')),  # CRUD-страницы hw1
    path('api/', include('api.urls')),  # API-маршруты hw2
]