from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Organization, Position, Membership
from django import forms


# =============== Organization Views ===============

class OrganizationListView(ListView):
    model = Organization
    template_name = 'orgapp/organization_list.html'
    context_object_name = 'organizations'
    paginate_by = 10


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = 'orgapp/organization_detail.html'
    context_object_name = 'organization'


class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization
    fields = ['name', 'description']
    template_name = 'orgapp/organization_form.html'
    success_url = reverse_lazy('orgapp:organization-list')


class OrganizationUpdateView(LoginRequiredMixin, UpdateView):
    model = Organization
    fields = ['name', 'description']
    template_name = 'orgapp/organization_form.html'
    success_url = reverse_lazy('orgapp:organization-list')


class OrganizationDeleteView(LoginRequiredMixin, DeleteView):
    model = Organization
    template_name = 'orgapp/organization_confirm_delete.html'
    success_url = reverse_lazy('orgapp:organization-list')


# =============== Position Views ===============

class PositionListView(ListView):
    model = Position
    template_name = 'orgapp/position_list.html'
    context_object_name = 'positions'
    paginate_by = 10


class PositionDetailView(DetailView):
    model = Position
    template_name = 'orgapp/position_detail.html'
    context_object_name = 'position'


class PositionCreateView(LoginRequiredMixin, CreateView):
    model = Position
    fields = ['title']
    template_name = 'orgapp/position_form.html'
    success_url = reverse_lazy('orgapp:position-list')


class PositionUpdateView(LoginRequiredMixin, UpdateView):
    model = Position
    fields = ['title']
    template_name = 'orgapp/position_form.html'
    success_url = reverse_lazy('orgapp:position-list')


class PositionDeleteView(LoginRequiredMixin, DeleteView):
    model = Position
    template_name = 'orgapp/position_confirm_delete.html'
    success_url = reverse_lazy('orgapp:position-list')


# =============== Membership Views ===============

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['user', 'organization', 'position']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'organization': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
        }


class MembershipListView(ListView):
    model = Membership
    template_name = 'orgapp/membership_list.html'
    context_object_name = 'memberships'
    paginate_by = 10


class MembershipDetailView(DetailView):
    model = Membership
    template_name = 'orgapp/membership_detail.html'
    context_object_name = 'membership'


class MembershipCreateView(LoginRequiredMixin, CreateView):
    model = Membership
    form_class = MembershipForm
    template_name = 'orgapp/membership_form.html'
    success_url = reverse_lazy('orgapp:membership-list')


class MembershipUpdateView(LoginRequiredMixin, UpdateView):
    model = Membership
    form_class = MembershipForm
    template_name = 'orgapp/membership_form.html'
    success_url = reverse_lazy('orgapp:membership-list')


class MembershipDeleteView(LoginRequiredMixin, DeleteView):
    model = Membership
    template_name = 'orgapp/membership_confirm_delete.html'
    success_url = reverse_lazy('orgapp:membership-list')