from rest_framework import viewsets
from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, OrganizationSerializer
from django.contrib.auth.models import User
from orgapp.models import Organization, Membership

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    @action(detail=False, methods=['get'], url_path='many-employees')
    def many_employees(self, request):
        """
        Возвращает список из 10 самых многочисленных по числу сотрудников организаций.
        """
        organizations = Organization.objects.annotate(
            employee_count=Count('membership')
        ).order_by('-employee_count')[:10]
        serializer = self.get_serializer(organizations, many=True)
        return Response(serializer.data)