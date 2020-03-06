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



# from game.views import *
# from users.views import *
# from apps.beheerder.views import *

# urlpatterns = [
	# url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	#algemeen
	# url(r'^registreren/$', registreren, name='registreren'),
	# url(r'^uitloggen/$', uitloggen, name='uitloggen'),
	#
	# #deelnemer
	# url(r'^$', homepage, name='homepage'),
	# url(r'^mijnteam/(?P<saved>\w+)/$', mijnteam, name='mijnteam'),
	# url(r'^mijnteam/$', mijnteam, name='mijnteam'),

	#beheerder
	#url(r'^beheerder/$', beheerder, name='beheerder'),
	#url(r'^beheerder/race_invoeren/(?P<race>\w+)/$', race_invoeren, name='race_invoeren'),
		
	#django-admin
	# url(r'^admin/', include(admin.site.urls)),
	
	#Bekijken van uitslagen
	# url(r'^update_waardes/(?P<race>\w+)/$', update_waardes, name='update_waardes'),
	# url(r'^update_waardes/$', update_waardes),
	#url(r'test/$', test)
# ]