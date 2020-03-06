from django.urls import path, include

from .views.account import HomepageView, MyTeamView
from .views.auth import LoginView, LogoutView, RegisterView


app_name = 'accounts'

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('my_team/', MyTeamView.as_view(), name='my_team'),
    path('auth/', include(([
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('register/', RegisterView.as_view(), name='register')],
        'auth')),
     )
]
