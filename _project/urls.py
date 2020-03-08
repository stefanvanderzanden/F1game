from django.contrib import admin
from django.urls import path, include

from apps.accounts.views.auth import LoginView, RegisterView, LogoutView
from apps.accounts.views.account import HomepageView
# from _project.views import HomepageView
# from apps.authentication.views import LoginView, LogoutView
# from apps.log_analyzer import urls as log_urls
# from apps.authentication import urls as user_urls

urlpatterns = [
    path('', include(('apps.accounts.urls', 'accounts'))),
    path('config/', include(('apps.game.urls', 'game'))),
    # path('login', LoginView.as_view(), name='login'),
    # path('register', RegisterView.as_view(), name='register'),
    # path('logout', LogoutView.as_view(), name='logout'),


    path('admin/', admin.site.urls),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('logs/', include(log_urls)),
    # path('users/', include(user_urls))
]
