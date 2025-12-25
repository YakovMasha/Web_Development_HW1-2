from rest_framework import serializers
from django.contrib.auth.models import User
from orgapp.models import Organization, Membership

class UserSerializer(serializers.ModelSerializer):
    organizations = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'organizations']

    def get_organizations(self, obj):
        """Возвращает список организаций, где состоит пользователь"""
        memberships = Membership.objects.filter(user=obj)
        return [m.organization.name for m in memberships]

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'description']