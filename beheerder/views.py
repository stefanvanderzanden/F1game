from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import datetime, time
from django.core.urlresolvers import reverse
import json
import urllib
from django.utils.datastructures import SortedDict

from users.forms import *
from game.forms import *
from game.models import *
from users.models import *
    

#update waardes coureurs
def update_waardes(request, race):
    if not race:
        url_kwali = 'http://ergast.com/api/f1/current/last/qualifying.json'
        url_race = 'http://ergast.com/api/f1/current/last/results.json'
        url_fastest_lap = 'http://ergast.com/api/f1/current/last/fastest/1/results.json'

    else:
        ronde = Race.objects.get(circuitId=race).circuitNr
        
        url_kwali = 'http://ergast.com/api/f1/current/'+ ronde +'/qualifying.json'
        url_race = 'http://ergast.com/api/f1/current/'+ ronde +'/results.json'
        url_fastest_lap = 'http://ergast.com/api/f1/current/'+ ronde +'/fastest/1/results.json'
        
    data_kwali = json.load(urllib.urlopen(url_kwali))
    data_race = json.load(urllib.urlopen(url_race))
    data_fastest_lap = json.load(urllib.urlopen(url_fastest_lap))
    
    circuitId = data_race['MRData']['RaceTable']['Races'][0]['Circuit']['circuitId']
    
    algemene_data = {
        'huidige_race': {'racenaam': data_kwali['MRData']['RaceTable']['Races'][0]['raceName'],
                 'snelste_ronde': data_fastest_lap['MRData']['RaceTable']['Races'][0]['Results'][0]['Driver']['givenName'] + ' ' + data_fastest_lap['MRData']['RaceTable']['Races'][0]['Results'][0]['Driver']['familyName'] }
    }

    scores_coureur_kwali = ScoreTabel.objects.filter(score_type='coureur', kwali_race='kwalificatie')
    scores_coureur_race = ScoreTabel.objects.filter(score_type='coureur', kwali_race='race')
    scores_team_kwali = ScoreTabel.objects.filter(score_type='motor', kwali_race='kwalificatie')
    scores_team_race = ScoreTabel.objects.filter(score_type='motor', kwali_race='race')
    
    
    uitslagen_coureurs = SortedDict()
    pos = 1 
    for x in data_race['MRData']['RaceTable']['Races'][0]['Results']:
        grid = x['grid']
        full_name = x['Driver']['givenName'] + ' ' + x['Driver']['familyName']
        coureur = Coureur.objects.get(driverId=x['Driver']['driverId'])
        oude_waarde = coureur.waarde
        plus_waarde = WaardeTabel.objects.filter(waarde_type='coureur').get(uitslag=pos).plus_waarde
        nieuwe_waarde = oude_waarde + plus_waarde
        
        status = x['status']
        
        uitslagen_coureurs[x['Driver']['driverId']] = {'coureur': full_name,
                                      'grid': grid,
                                      'positie': pos,
                                      'status': status,
                                      'punten_kwali': scores_coureur_kwali.get(uitslag=grid).punten,
                                      'punten_race': scores_coureur_race.get(uitslag=pos).punten,
                                      'oude_waarde': oude_waarde,
                                      'nieuwe_waarde': nieuwe_waarde
                                      }
        pos += 1
        
    
    uitslagen_teams = SortedDict()
    opgetelde_plus_waarde = {}
    pos = 1
    for x in data_race['MRData']['RaceTable']['Races'][0]['Results']:
        team = Team.objects.get(teamId=x['Constructor']['constructorId'])
        oude_waarde = team.waarde
        plus_waarde = WaardeTabel.objects.filter(waarde_type='motor').get(uitslag=pos).plus_waarde
        if x['Constructor']['constructorId'] in uitslagen_teams:
            opgetelde_plus_waarde[x['Constructor']['constructorId']] += plus_waarde
        else:
            opgetelde_plus_waarde[x['Constructor']['constructorId']] = plus_waarde
        uitslagen_teams[x['Constructor']['constructorId']] = {'team': x['Constructor']['name'],
                                      'oude_waarde': oude_waarde,
                                      'nieuwe_waarde': oude_waarde + opgetelde_plus_waarde[x['Constructor']['constructorId']]
                                      }
        
        pos += 1

        
    '''
    Hieronder worden alle waardes opgeslagen
    '''
    if request.method == 'POST':
        circuitId = data_race['MRData']['RaceTable']['Races'][0]['Circuit']['circuitId']
        race = Race.objects.get(circuitId=circuitId)

        scores_coureur_kwali = ScoreTabel.objects.filter(score_type='coureur', kwali_race='kwalificatie')
        scores_coureur_race = ScoreTabel.objects.filter(score_type='coureur', kwali_race='race')
        scores_team_kwali = ScoreTabel.objects.filter(score_type='motor', kwali_race='kwalificatie')
        scores_team_race = ScoreTabel.objects.filter(score_type='motor', kwali_race='race')

        
        #1. Uitslag per coureur tabel moet gevuld/geupdate worden
        pos=1
        update_waarde_teams = {}
        for x in data_race['MRData']['RaceTable']['Races'][0]['Results']:
            coureur = Coureur.objects.get(driverId=x['Driver']['driverId'])
            positie_kwali = x['grid']
            positie_race = pos
            status = x['status']
            punten_kwali_coureur = scores_coureur_kwali.get(uitslag=grid).punten
            punten_race_coureur = scores_coureur_race.get(uitslag=pos).punten
            punten_kwali_team = scores_team_kwali.get(uitslag=grid).punten
            punten_race_team = scores_team_race.get(uitslag=pos).punten
            UitslagPerCoureur.objects.create_uitslag(coureur,
                                 race,
                                 positie_kwali,
                                 positie_race,
                                 status,
                                 punten_kwali_coureur,
                                 punten_race_coureur,
                                 punten_kwali_team,
                                 punten_race_team)
            '''
            10-06-2013 TIJDELIJK ERUIT GECOMMENTARIEERD VOOR TESTDOELEINDEN 
            
            coureur = Coureur.objects.get(driverId=x['Driver']['driverId'])
            oude_waarde = coureur.waarde
            plus_waarde = WaardeTabel.objects.filter(waarde_type='coureur').get(uitslag=pos).plus_waarde
            nieuwe_waarde = oude_waarde + plus_waarde
            VerloopCoureurs.objects.create_verloop_coureur(coureur, race, oude_waarde, nieuwe_waarde)
            coureur.waarde = nieuwe_waarde
            coureur.save()
            
            team = Team.objects.get(teamId=x['Constructor']['constructorId'])
            plus_waarde = WaardeTabel.objects.filter(waarde_type='motor').get(uitslag=pos).plus_waarde
            if x['Constructor']['constructorId'] in update_waarde_teams:
                update_waarde_teams[x['Constructor']['constructorId']] += plus_waarde
                oude_waarde = team.waarde
                opgetelde_plus_waarde = update_waarde_teams[x['Constructor']['constructorId']]
                nieuwe_waarde = oude_waarde + opgetelde_plus_waarde
                VerloopTeams.objects.create_verloop_team(team, race, oude_waarde, nieuwe_waarde)
                team.waarde = nieuwe_waarde
                team.save()
            else:
                update_waarde_teams[x['Constructor']['constructorId']] = plus_waarde
            '''
            pos += 1

        
        #2. Maak voor iedereen een scoreperrace
        uitslagpercoureur = UitslagPerCoureur.objects.filter(race__circuitId=circuitId)
        trivia_goede_antwoord = Trivia.objects.get(race__circuitId=circuitId).correct_antwoord
        snelste_coureur = data_fastest_lap['MRData']['RaceTable']['Races'][0]['Results'][0]['Driver']['driverId']
        snelste_pitstop = ManueleInput.objects.get(race=race).snelste_pitstop
        
        for x in UserProfile.objects.filter(mijnteam__coureur1__isnull=False,
                            mijnteam__coureur2__isnull=False,
                            mijnteam__team1__isnull=False,
                            mijnteam__team2__isnull=False):
            user = x.user
            coureur1 = x.mijnteam.coureur1
            coureur2 = x.mijnteam.coureur2
            team1 = x.mijnteam.team1
            team2 = x.mijnteam.team2
            
            trivia = x.mijnteam.trivia_antwoord
            snelste_coureur = x.mijnteam.snelste_coureur
            snelste_pitstop = x.mijnteam.snelste_pitstop
            
            #hier in de loop voor berekening van punten HOUD REKENING MET JOKERS
            
            mijnteam = MijnTeam.objects.get(userprofile=x)
            coureur1_punten_kwali = uitslagpercoureur.get(coureur=mijnteam.coureur1).punten_kwali_coureur
            coureur1_punten_race = uitslagpercoureur.get(coureur=mijnteam.coureur1).punten_race_coureur
            coureur2_punten_kwali = uitslagpercoureur.get(coureur=mijnteam.coureur2).punten_kwali_coureur
            coureur2_punten_race = uitslagpercoureur.get(coureur=mijnteam.coureur2).punten_race_coureur
            
            team1_coureur1_punten_kwali = uitslagpercoureur.filter(coureur__team=mijnteam.team1)[0].punten_kwali_team
            team1_coureur1_punten_race = uitslagpercoureur.filter(coureur__team=mijnteam.team1)[0].punten_race_team
            team1_coureur2_punten_kwali = uitslagpercoureur.filter(coureur__team=mijnteam.team1)[1].punten_kwali_team
            team1_coureur2_punten_race = uitslagpercoureur.filter(coureur__team=mijnteam.team1)[1].punten_race_team
            
            team2_coureur1_punten_kwali = uitslagpercoureur.filter(coureur__team=mijnteam.team2)[0].punten_kwali_team
            team2_coureur1_punten_race = uitslagpercoureur.filter(coureur__team=mijnteam.team2)[0].punten_race_team
            team2_coureur2_punten_kwali = uitslagpercoureur.filter(coureur__team=mijnteam.team2)[1].punten_kwali_team
            team2_coureur2_punten_race = uitslagpercoureur.filter(coureur__team=mijnteam.team2)[1].punten_race_team
            
            if mijnteam.joker_coureur1:
                coureur1_punten_kwali = coureur1_punten_kwali * 2
                coureur1_punten_race = coureur1_punten_race * 2
                x.jokers -= 1
                
            if mijnteam.joker_coureur2:
                coureur2_punten_kwali = coureur2_punten_kwali * 2
                coureur2_punten_race = coureur2_punten_race * 2
                x.jokers -= 1
                
            if mijnteam.joker_team1:
                team1_coureur1_punten_kwali = team1_coureur1_punten_kwali * 2
                team1_coureur1_punten_race = team1_coureur1_punten_race * 2
                team1_coureur2_punten_kwali = team1_coureur2_punten_kwali * 2
                team1_coureur2_punten_race = team1_coureur2_punten_race * 2
                x.jokers -= 1
            
            if mijnteam.joker_team2:
                team2_coureur1_punten_kwali = team2_coureur1_punten_kwali * 2
                team2_coureur1_punten_race = team2_coureur1_punten_race * 2
                team2_coureur2_punten_kwali = team2_coureur2_punten_kwali * 2
                team2_coureur2_punten_race = team2_coureur2_punten_race * 2
                x.jokers -= 1
            
            #DriveThroughs
            
            
            
            verdiende_punten_kwali = (coureur1_punten_kwali + coureur2_punten_kwali + team1_coureur1_punten_kwali +
            team1_coureur2_punten_kwali + team2_coureur1_punten_kwali + team2_coureur2_punten_kwali)
            
            verdiende_punten_race = (coureur1_punten_race + coureur2_punten_race + team1_coureur1_punten_race +
            team1_coureur2_punten_race + team2_coureur1_punten_race + team2_coureur2_punten_race)
            
            verdiende_punten_totaal = verdiende_punten_kwali + verdiende_punten_race    
            
            if x.punten:
                oude_punten = x.punten
            else:
                oude_punten = 0
        
            nieuwe_punten = oude_punten + verdiende_punten_totaal
            
            
            ScorePerRace.objects.create_score(race=race,
                      user=user,
                      coureur1=coureur1,
                      coureur2=coureur2,
                      team1=team1,
                      team2=team2,
                      coureur1_punten_kwali=coureur1_punten_kwali,
                      coureur1_punten_race=coureur1_punten_race,
                      coureur2_punten_kwali=coureur2_punten_kwali,
                      coureur2_punten_race=coureur2_punten_race,
                      team1_coureur1_punten_kwali=team1_coureur1_punten_kwali,
                      team1_coureur1_punten_race=team1_coureur1_punten_race,
                      team1_coureur2_punten_kwali=team1_coureur2_punten_kwali,
                      team1_coureur2_punten_race=team1_coureur2_punten_race,
                      team2_coureur1_punten_kwali=team2_coureur1_punten_kwali,
                      team2_coureur1_punten_race=team2_coureur1_punten_race,
                      team2_coureur2_punten_kwali=team2_coureur2_punten_kwali,
                      team2_coureur2_punten_race=team2_coureur2_punten_race,
                      trivia=trivia,
                      snelste_coureur=snelste_coureur,
                      snelste_pitstop=snelste_pitstop,
                      oude_punten=oude_punten,
                      totaal_kwali=verdiende_punten_kwali,
                      totaal_race=verdiende_punten_race,
                      totaal=verdiende_punten_totaal)
            
            

            x.punten = nieuwe_punten 
            x.budget = x.budget + (verdiende_punten_totaal * 50000)            
            
            if x.mijnteam.trivia_antwoord == trivia_goede_antwoord:
                x.punten += 25
            if x.mijnteam.snelste_coureur == snelste_coureur:
                x.punten += 25
            if x.mijnteam.snelste_pitstop == snelste_pitstop:
                x.punten += 25
                
            x.kosten = mijnteam.coureur1.waarde + mijnteam.coureur2.waarde + mijnteam.team1.waarde + mijnteam.team2.waarde
            x.balans = x.budget - x.kosten            
            x.save()
            
            mijnteam.trivia_antwoord = None
            mijnteam.save()
            
        race.geupdate = True
        race.is_aankomende_race = False
        race.save()
        
        circuitNr = int(race.circuitNr)+1
        aankomende_race = Race.objects.get(circuitNr=circuitNr)
        aankomende_race.is_aankomende_race = True    
        aankomende_race.save()
            
                
    return render_to_response('beheerder/beheerder_update_waardes.html',{'algemene_data': algemene_data,
                                         'uitslagen_coureurs': uitslagen_coureurs,
                                         'uitslagen_teams': uitslagen_teams,
                                         }, context_instance=RequestContext(request))
        
    #extra idee --> hoogste snelheid op het parcour
