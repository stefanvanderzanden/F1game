from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from game.views import *
from users.views import *
from beheerder.views import *

urlpatterns = patterns('',
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	#algemeen
	url(r'^registreren/$', registreren, name='registreren'),
	url(r'^uitloggen/$', uitloggen, name='uitloggen'),
	
	#deelnemer	
	url(r'^$', homepage, name='homepage'),
	url(r'^mijnteam/(?P<saved>\w+)/$', mijnteam, name='mijnteam'),
	url(r'^mijnteam/$', mijnteam, name='mijnteam'),

	#beheerder
	#url(r'^beheerder/$', beheerder, name='beheerder'),
	#url(r'^beheerder/race_invoeren/(?P<race>\w+)/$', race_invoeren, name='race_invoeren'),
		
	#django-admin
	url(r'^admin/', include(admin.site.urls)),
	
	#Bekijken van uitslagen
	url(r'^update_waardes/(?P<race>\w+)/$', update_waardes, name='update_waardes'),
	url(r'^update_waardes/$', update_waardes),
	#url(r'test/$', test)
)
