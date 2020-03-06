from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.game.models import Driver


class HomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'account/homepage.html'

    def get_context_data(self, **kwargs):
        drivers = Driver.objects.all()
        return super(HomepageView, self).get_context_data(
            drivers=drivers,
            **kwargs)


class MyTeamView(TemplateView):
    template_name = 'account/my_team.html'
