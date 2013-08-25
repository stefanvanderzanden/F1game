from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib import admin

from game.models import Coureur, Team, Race, Trivia


class ScorePerRaceManager(models.Manager):
	def create_score(self, race, user,
			 coureur1, coureur2, team1, team2,
			 coureur1_punten_kwali, coureur1_punten_race,
			 coureur2_punten_kwali, coureur2_punten_race,
			 team1_coureur1_punten_kwali, team1_coureur1_punten_race,
			 team1_coureur2_punten_kwali, team1_coureur2_punten_race,
			 team2_coureur1_punten_kwali, team2_coureur1_punten_race,
			 team2_coureur2_punten_kwali, team2_coureur2_punten_race,
			 trivia, snelste_coureur, snelste_pitstop, oude_punten,
			 totaal_kwali, totaal_race, totaal):
		
		score = self.create(race=race,
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
				      totaal_kwali=totaal_kwali,
				      totaal_race=totaal_race,
				      totaal=totaal)
		return score


class ScorePerRace(models.Model):
	race = models.ForeignKey(Race, related_name='scoreperrace_race')
	user = models.ForeignKey(User, related_name='scoreperrace_user', null=True)
	
	coureur1 = models.ForeignKey(Coureur, related_name='scoreperrace_coureur1', null=True)
	coureur2 = models.ForeignKey(Coureur, related_name='scoreperrace_coureur2', null=True)
	team1 = models.ForeignKey(Team, related_name='scoreperrace_team1', null=True)
	team2 = models.ForeignKey(Team, related_name='scoreperrace_team2', null=True)

	coureur1_punten_kwali = models.IntegerField(max_length=4, default=0)
	coureur1_punten_race = models.IntegerField(max_length=4, default=0)
	coureur2_punten_kwali = models.IntegerField(max_length=4, default=0)
	coureur2_punten_race = models.IntegerField(max_length=4, default=0)
	
	team1_coureur1_punten_kwali = models.IntegerField(max_length=4, default=0)
	team1_coureur1_punten_race = models.IntegerField(max_length=4, default=0)
	team1_coureur2_punten_kwali = models.IntegerField(max_length=4, default=0)
	team1_coureur2_punten_race = models.IntegerField(max_length=4, default=0)

	team2_coureur1_punten_kwali = models.IntegerField(max_length=4, default=0)
	team2_coureur1_punten_race = models.IntegerField(max_length=4, default=0)
	team2_coureur2_punten_kwali = models.IntegerField(max_length=4, default=0)
	team2_coureur2_punten_race = models.IntegerField(max_length=4, default=0)

	trivia = models.CharField(max_length=1, blank=True, null=True, choices=(('A','A'), ('B','B'), ('C','C'), ('D','D')))
	snelste_coureur = models.ForeignKey(Coureur, related_name='scoreperrace_snelstecoureur', null=True)
	snelste_pitstop = models.ForeignKey(Team, related_name='scoreperrace_snelstepitstop', null=True)
	
	oude_punten = models.IntegerField(max_length=4, default=0)
	totaal_kwali = models.IntegerField(max_length=4)
	totaal_race = models.IntegerField(max_length=4)
	totaal = models.IntegerField(max_length=4) #Plus Trivia en extra's
	
	objects = ScorePerRaceManager()


	def __unicode__(self):
		return self.race.naam
	
	

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	
	geslacht = models.CharField(max_length=1)
	tussenvoegsel = models.CharField(max_length=30, blank=True, null=True)
	volledige_naam = models.CharField(max_length=120)
	volledige_achternaam = models.CharField(max_length=200)
	punten = models.IntegerField(max_length=6, blank=True, null=True)
	budget = models.IntegerField(max_length=15, blank=True, null=True)
	jokers = models.IntegerField(max_length=1, blank=True, null=True)
	kosten = models.IntegerField(max_length=15, blank=True, null=True)
	balans = models.IntegerField(max_length=15, blank=True, null=True)
	
	def __unicode__(self):
		return self.volledige_naam

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)        
        
class MijnTeam(models.Model):
	TRIVIA_OPTIES = (('A','A'), ('B','B'), ('C','C'), ('D','D'))
	userprofile = models.OneToOneField(UserProfile)
	
	coureur1 = models.ForeignKey(Coureur, blank=True, null=True, related_name='mijnteam_coureur1')
	coureur2 = models.ForeignKey(Coureur, blank=True, null=True, related_name='mijnteam_coureur2')
	team1 = models.ForeignKey(Team, blank=True, null=True, related_name='mijnteam_team1')
	team2 = models.ForeignKey(Team, blank=True, null=True, related_name='mijnteam_team2')
	joker_coureur1 = models.BooleanField(default=False)
	joker_coureur2 = models.BooleanField(default=False)
	joker_team1 = models.BooleanField(default=False)
	joker_team2 = models.BooleanField(default=False)
	snelste_coureur = models.ForeignKey(Coureur, blank=True, null=True, related_name='mijnteam_snelstecoureur')
	snelste_pitstop = models.ForeignKey(Team, blank=True, null=True, related_name='mijnteam_snelstepitstop')
	trivia_antwoord = models.CharField(max_length=1, blank=True, null=True, choices=TRIVIA_OPTIES)


'''
ADMNIN SPULLEN
'''



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['volledige_achternaam', 'geslacht', 'punten', 'budget', 'kosten', 'jokers']
    ordering = ['volledige_achternaam']


class MijnTeamAdmin(admin.ModelAdmin):
	list_display =  ['userprofile', 'coureur1', 'coureur2', 'team1', 'team2']

class ScorePerRaceAdmin(admin.ModelAdmin):
	list_display = ['race', 'user', 'totaal']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(MijnTeam, MijnTeamAdmin)
admin.site.register(ScorePerRace, ScorePerRaceAdmin)
