from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import logout

from apps.accounts.forms import *

from apps.accounts.models import *


def registreren(request):
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			if cd['wachtwoord'] == cd['herhaal_wachtwoord']:
				voornaam = cd['voornaam']
				achternaam = cd['achternaam']
				tussenvoegsel = cd['tussenvoegsel']
				if tussenvoegsel:
					volledige_achternaam = tussenvoegsel + ' ' + achternaam
					volledige_naam = voornaam + ' ' + tussenvoegsel + ' ' + achternaam
				else:
					volledige_achternaam = achternaam
					volledige_naam = voornaam + achternaam

				email = cd['email']
				geslacht = cd['geslacht']
				wachtwoord = cd['wachtwoord']
				username = email.split('@')[0]
				user = User.objects.create_user(username, email, wachtwoord)
				user.first_name = voornaam
				user.last_name = achternaam
				user.is_active = True
				user.is_staff = False
				user.is_superuser = False
				user.save()

				userprofile = user.get_profile()
				userprofile.budget = 100000000
				userprofile.jokers = 6
				userprofile.balans = 100000000
				userprofile.geslacht = geslacht
				userprofile.volledige_achternaam = volledige_achternaam
				userprofile.volledige_naam = volledige_naam
				userprofile.tussenvoegsel = tussenvoegsel
				userprofile.save()
				
				mijnteam = MijnTeam()
				mijnteam.userprofile = userprofile
				mijnteam.coureur1 = None
				mijnteam.coureur2 = None
				mijnteam.team1 = None
				mijnteam.team2 = None
				mijnteam.save()
				
			return HttpResponseRedirect("/")
	else:
		form = CreateUserForm()
	return render_to_response("registratie/registreren.html", {'form': form} , context_instance=RequestContext(request))
	
def uitloggen(request):
	logout(request)
	return HttpResponseRedirect('/')


