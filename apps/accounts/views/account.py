from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from apps.accounts.forms import DriverSelectForm
from apps.game.models import Driver


class HomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'account/homepage.html'

    def get_context_data(self, **kwargs):
        drivers = Driver.objects.all().order_by('team__order', 'order')
        return super(HomepageView, self).get_context_data(
            drivers=drivers,
            **kwargs)


class MyTeamView(FormView):
    template_name = 'account/my_team.html'
    form_class = DriverSelectForm
    success_url = reverse_lazy('accounts:home')
