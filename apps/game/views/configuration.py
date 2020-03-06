from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from apps.game.models import Driver, Team


class TeamListView(LoginRequiredMixin, ListView):
    template_name = 'game/configuration/teams/list.html'
    model = Team
    ordering = ['order']


class TeamAddView(LoginRequiredMixin, CreateView):
    model = Team
    template_name = 'game/configuration/teams/add.html'
    fields = ['name', 'value', 'description', 'image', 'order']
    success_url = reverse_lazy('game:teams:list')


class TeamEditView(LoginRequiredMixin, UpdateView):
    model = Team
    template_name = 'game/configuration/teams/edit.html'
    pk_url_kwarg = 'team_id'
    fields = ['name', 'value', 'description', 'image', 'order']
    success_url = reverse_lazy('game:teams:list')


class DriverListView(LoginRequiredMixin, ListView):
    template_name = 'game/configuration/drivers/list.html'
    model = Driver
    ordering = ['team__order', 'order']


class DriverAddView(LoginRequiredMixin, CreateView):
    model = Driver
    template_name = 'game/configuration/drivers/add.html'
    fields = ['name', 'number', 'value', 'team', 'description', 'image', 'active', 'order']
    success_url = reverse_lazy('game:drivers:add')


class DriverEditView(LoginRequiredMixin, UpdateView):
    model = Driver
    template_name = 'game/configuration/drivers/edit.html'
    pk_url_kwarg = 'driver_id'
    fields = ['name', 'number', 'value', 'team', 'description', 'image', 'active', 'order']
    success_url = reverse_lazy('game:drivers:list')


