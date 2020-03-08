from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from apps.game.models import Driver, Team, Season


class SeasonListView(LoginRequiredMixin, ListView):
    template_name = 'game/configuration/seasons/list.html'
    model = Season
    ordering = ['year']


class SeasonAddView(LoginRequiredMixin, CreateView):
    model = Season
    template_name = 'game/configuration/seasons/add.html'
    fields = ['year', 'active']
    success_url = reverse_lazy('game:seasons:list')


class SeasonEditView(LoginRequiredMixin, CreateView):
    model = Season
    template_name = 'game/configuration/seasons/edit.html'
    fields = ['year', 'active']
    success_url = reverse_lazy('game:seasons:list')


class TeamListView(LoginRequiredMixin, ListView):
    template_name = 'game/configuration/teams/list.html'
    model = Team
    ordering = ['order']


class TeamAddView(LoginRequiredMixin, CreateView):
    model = Team
    template_name = 'game/configuration/teams/add.html'
    fields = ['name', 'value', 'description', 'image', 'order', 'season']
    success_url = reverse_lazy('game:teams:list')


class TeamEditView(LoginRequiredMixin, UpdateView):
    model = Team
    template_name = 'game/configuration/teams/edit.html'
    pk_url_kwarg = 'team_id'
    fields = ['name', 'value', 'description', 'image', 'order', 'season']
    success_url = reverse_lazy('game:teams:list')


class DriverListView(LoginRequiredMixin, ListView):
    template_name = 'game/configuration/drivers/list.html'
    model = Driver
    ordering = ['team__order', 'order']


class DriverAddView(LoginRequiredMixin, CreateView):
    model = Driver
    template_name = 'game/configuration/drivers/add.html'
    fields = ['name', 'number', 'value', 'team', 'description', 'image', 'active', 'order', 'season']
    success_url = reverse_lazy('game:drivers:add')


class DriverEditView(LoginRequiredMixin, UpdateView):
    model = Driver
    template_name = 'game/configuration/drivers/edit.html'
    pk_url_kwarg = 'driver_id'
    fields = ['name', 'number', 'value', 'team', 'description', 'image', 'active', 'order', 'season']
    success_url = reverse_lazy('game:drivers:list')
