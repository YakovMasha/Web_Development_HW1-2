from django.contrib import admin
from .models import Organization, Position, Membership


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization', 'position', 'joined_at')
    list_filter = ('organization', 'position', 'joined_at')
    search_fields = ('user__username', 'organization__name', 'position__title')