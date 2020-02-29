from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.urlresolvers import reverse
from apps.game.models import *
from users.forms import *


@login_required
def homepage(request):
    if not request.user.is_staff:
        userprofile = UserProfile.objects.get(user=request.user.id)
        mijnteam = MijnTeam.objects.get(userprofile=userprofile)
        return render_to_response('homepage.html', {'userprofile':userprofile, 'mijnteam': mijnteam}, context_instance=RequestContext(request))
    else:
        if request.method == 'POST':  
            coureurslist = [
            {'driverId': 'alonso', 'waarde': 50000000},
            {'driverId': 'vettel', 'waarde': 50000000},
            {'driverId': 'raikkonen', 'waarde': 47000000},
            {'driverId': 'button', 'waarde': 42500000},
            {'driverId': 'webber', 'waarde': 40000000},
            {'driverId': 'massa', 'waarde': 37500000},
            {'driverId': 'perez', 'waarde': 37500000},
            {'driverId': 'hamilton', 'waarde': 35000000},
            {'driverId': 'rosberg', 'waarde': 35000000},
            {'driverId': 'grosjean', 'waarde': 35000000},
            {'driverId': 'hulkenberg', 'waarde': 27500000},
            {'driverId': 'maldonado', 'waarde': 25000000},
            {'driverId': 'resta', 'waarde': 25000000},
            {'driverId': 'gutierrez', 'waarde': 25000000},
            {'driverId': 'sutil', 'waarde': 25000000},
            {'driverId': 'bottas', 'waarde': 21000000},
            {'driverId': 'ricciardo', 'waarde': 21000000},
            {'driverId': 'vergne', 'waarde': 20000000},
            {'driverId': 'pic', 'waarde': 16000000},
            {'driverId': 'garde', 'waarde': 15000000},
            {'driverId': 'chilton', 'waarde': 14000000},
            {'driverId': 'jules_bianchi', 'waarde': 13000000},
            ]
            
            for coureur in coureurslist:
                c = Coureur.objects.get(driverId=coureur['driverId'])
                c.waarde = coureur['waarde']
                c.save()
            
            teamslist = [
            {'teamId': 'red_bull', 'waarde': 50000000},
            {'teamId': 'ferrari', 'waarde': 47500000},
            {'teamId': 'mclaren', 'waarde': 45000000},
            {'teamId': 'mercedes', 'waarde': 42500000},
            {'teamId': 'lotus_f1', 'waarde': 42500000},
            {'teamId': 'sauber', 'waarde': 37500000},
            {'teamId': 'force_india', 'waarde': 35000000},
            {'teamId': 'williams', 'waarde': 32500000},
            {'teamId': 'toro_rosso', 'waarde': 25000000},
            {'teamId': 'caterham', 'waarde': 14000000},
            {'teamId': 'marussia', 'waarde': 13000000},
            ]

            for team in teamslist:
                t = Team.objects.get(teamId=team['teamId'])
                t.waarde = team['waarde']
                t.save()

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
        
        
