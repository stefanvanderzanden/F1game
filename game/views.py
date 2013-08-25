from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import datetime, time
from django.utils import timezone
from django.core.urlresolvers import reverse
import urllib2
from game.models import *
from users.forms import *


@login_required
def homepage(request):
	if not request.user.is_staff:
		userprofile = UserProfile.objects.get(user=request.user.id)
		mijnteam = MijnTeam.objects.get(userprofile=userprofile)
		return render_to_response('homepage.html', {'userprofile':userprofile, 'mijnteam': mijnteam}, context_instance=RequestContext(request))
	else:
		return render_to_response('beheerder/beheerder_home.html', {'user': request.user}, context_instance=RequestContext(request))
	
	

@login_required
def mijnteam(request, saved=None):
	userprofile = UserProfile.objects.get(user=request.user.id)
	berichten = {}			
	#Bepaal huidige race voor Trivia
	race = Race.objects.get(is_aankomende_race=True)
	trivia = Trivia.objects.get(race__circuitId=race.circuitId)

	if request.method == 'POST':
		form = MijnTeamForm(request.user, request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			mijnteam = MijnTeam.objects.filter(userprofile=userprofile)
				
			if len(mijnteam) == 0:
				mijnteam = MijnTeam()
				mijnteam.userprofile = userprofile
			elif len(mijnteam) == 1:
			    mijnteam = mijnteam[0]	
			
			mijnteam.coureur1 = cd['coureur1']
			mijnteam.coureur2 = cd['coureur2']
			mijnteam.team1 = cd['team1']
			mijnteam.team2 = cd['team2']
			mijnteam.snelste_coureur = cd['snelste_coureur']
			mijnteam.snelste_pitstop = cd['snelste_pitstop']
			mijnteam.trivia_antwoord = cd['trivia_antwoord']
			mijnteam.joker_coureur1 = cd['joker_coureur1']
			mijnteam.joker_coureur2 = cd['joker_coureur2']
			mijnteam.joker_team1 = cd['joker_team1']
			mijnteam.joker_team2 = cd['joker_team2']
			
			userprofile.kosten = (int(mijnteam.coureur1.waarde) + int(mijnteam.coureur2.waarde) + int(mijnteam.team1.waarde) + int(mijnteam.team2.waarde))
			userprofile.balans = userprofile.budget - userprofile.kosten
						
			userprofile.save()
			mijnteam.save()		
			

			berichten['succes'] = True			
			return render_to_response('mijnteam.html', {'form': form,
								    'mijnteam': mijnteam,
								    'userprofile': userprofile,
								    'trivia': trivia,
								    'berichten':berichten}, context_instance=RequestContext(request))
		else:
			mijnteam = MijnTeam.objects.get(userprofile=userprofile)
			form = MijnTeamForm(request.user, request.POST, instance=mijnteam)
			return render_to_response('mijnteam.html', {'form': form,
								    'mijnteam': mijnteam,
								    'userprofile': userprofile,
								    'trivia': trivia,
								    'berichten': berichten }, context_instance=RequestContext(request))
	else:
		mijnteam = MijnTeam.objects.get(userprofile=userprofile)
		form = MijnTeamForm(request.user, instance=mijnteam)
		
		
		
		return render_to_response('mijnteam.html', {'form': form,
							    'mijnteam': mijnteam,
							    'userprofile': userprofile,
							    'berichten': berichten,
							    'trivia': trivia }, context_instance=RequestContext(request))
		
		
