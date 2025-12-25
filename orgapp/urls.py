from django.urls import path
from . import views

app_name = 'orgapp'

urlpatterns = [
    # Organization
    path('organizations/', views.OrganizationListView.as_view(), name='organization-list'),
    path('organizations/<int:pk>/', views.OrganizationDetailView.as_view(), name='organization-detail'),
    path('organizations/create/', views.OrganizationCreateView.as_view(), name='organization-create'),
    path('organizations/<int:pk>/update/', views.OrganizationUpdateView.as_view(), name='organization-update'),
    path('organizations/<int:pk>/delete/', views.OrganizationDeleteView.as_view(), name='organization-delete'),

    # Position
    path('positions/', views.PositionListView.as_view(), name='position-list'),
    path('positions/<int:pk>/', views.PositionDetailView.as_view(), name='position-detail'),
    path('positions/create/', views.PositionCreateView.as_view(), name='position-create'),
    path('positions/<int:pk>/update/', views.PositionUpdateView.as_view(), name='position-update'),
    path('positions/<int:pk>/delete/', views.PositionDeleteView.as_view(), name='position-delete'),

    # Membership
    path('memberships/', views.MembershipListView.as_view(), name='membership-list'),
    path('memberships/<int:pk>/', views.MembershipDetailView.as_view(), name='membership-detail'),
    path('memberships/create/', views.MembershipCreateView.as_view(), name='membership-create'),
    path('memberships/<int:pk>/update/', views.MembershipUpdateView.as_view(), name='membership-update'),
    path('memberships/<int:pk>/delete/', views.MembershipDeleteView.as_view(), name='membership-delete'),
]