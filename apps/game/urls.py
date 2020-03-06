from django.urls import path, include

from apps.game.views.configuration import *

app_name = 'game'

urlpatterns = [
    # path('', HomepageView.as_view(), name='home'),
    # path('my_team/', MyTeamView.as_view(), name='my_team'),
    path('drivers/', include(([
        path('', DriverListView.as_view(), name='list'),
        path('add/', DriverAddView.as_view(), name='add'),
        path('edit/<int:driver_id>/', DriverEditView.as_view(), name='edit'),
        # path('delete/<int:driver_id>', DriverDeleteView.as_view(), name='delete'),
        ], 'drivers')),
     ),
    path('teams/', include(([
        path('', TeamListView.as_view(), name='list'),
        path('add/', TeamAddView.as_view(), name='add'),
        path('edit/<int:team_id>/', TeamEditView.as_view(), name='edit'),
        ], 'teams')),
    )
]
