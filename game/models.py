from django.db import models
from django.contrib import admin


class Team(models.Model):
	naam = models.CharField(max_length=120)
	waarde = models.IntegerField(max_length=10)
	beschrijving = models.TextField(max_length=10000)	
	teamId = models.CharField(max_length=20, default='id')
	
	def __unicode__(self):
		return self.naam
	
class Coureur(models.Model):
	naam = models.CharField(max_length=120)
	waarde = models.IntegerField(max_length=10)
	team = models.ForeignKey(Team)
	beschrijving = models.TextField(max_length=10000)
	driverId = models.CharField(max_length=20, default='id')

	def __unicode__(self):
		return self.naam

class Race(models.Model):
	naam = models.CharField(max_length=130) 
	tag = models.CharField(max_length=30)
	circuitId = models.CharField(max_length=20, default='id')
	circuitNr = models.CharField(max_length=20, default='1')
	start = models.DateTimeField()
	beschrijving = models.TextField(max_length=10000)
	is_aankomende_race=models.BooleanField(default=False)
	geupdate = models.BooleanField(default=False)
	
	
	def __unicode__(self):
		return self.naam	
	

class ScoreTabel(models.Model):
	score_type = models.CharField(max_length=20, choices=(('coureur', 'Coureur'), ('motor', 'Motor')))
	kwali_race = models.CharField(max_length=20, choices=(('kwalificatie', 'Kwalificatie'), ('race', 'Race')))
	uitslag = models.IntegerField(max_length=2)
	punten = models.IntegerField(max_length=3)
	
class WaardeTabel(models.Model):
	waarde_type = models.CharField(max_length=20, choices=(('coureur', 'Coureur'), ('motor', 'Motor')))
	uitslag = models.IntegerField(max_length=2)
	plus_waarde = models.IntegerField(max_length=10)
	
class UitslagPerCoureurManager(models.Manager):
	def create_uitslag(self, coureur, race, positie_kwali, positie_race, status, punten_kwali_coureur,
			   punten_race_coureur, punten_kwali_team, punten_race_team):
		uitslag = self.create(coureur=coureur,
				      race=race,
				      positie_kwali=positie_kwali,
				      positie_race=positie_race,
				      status=status,
				      punten_kwali_coureur=punten_kwali_coureur,
				      punten_race_coureur=punten_race_coureur,
				      punten_kwali_team = punten_kwali_team,
				      punten_race_team = punten_race_team)
		return uitslag


class UitslagPerCoureur(models.Model):
	coureur = models.ForeignKey(Coureur, related_name='uitslagcoureur_coureur')
	race = models.ForeignKey(Race, related_name='uitslagcoureur_race')
	positie_kwali = models.IntegerField(max_length=2)
	positie_race = models.IntegerField(max_length=2)
	drivethrough = models.BooleanField(default=False)
	status = models.CharField(max_length=100)
	punten_kwali_coureur = models.IntegerField(max_length=4, default=0)
	punten_race_coureur = models.IntegerField(max_length=4, default=0)
	punten_kwali_team = models.IntegerField(max_length=4, default=0)
	punten_race_team = models.IntegerField(max_length=4, default=0)
	
	objects = UitslagPerCoureurManager()
	
	class Meta:
		unique_together = ('coureur', 'race')
	
class ManueleInput(models.Model):
	race = models.ForeignKey(Race, related_name='manueleinput_race')
	#snelste_coureur = models.ForeignKey(Coureur, null=True)
	snelste_pitstop = models.ForeignKey(Team, related_name='manueleinput_team')
	
class DriveThrough(models.Model):
	race = models.ForeignKey(Race, related_name='drivethrough_race')
	coureur = models.ForeignKey(Coureur, related_name='drivethrough_coureur')



class VerloopCoureursManager(models.Manager):
	def create_verloop_coureur(self, coureur, race, start_waarde, eind_waarde):
		verloop_coureur = self.create(coureur=coureur,
				      race=race,
				      start_waarde=start_waarde,
				      eind_waarde=eind_waarde)
		return verloop_coureur


class VerloopCoureurs(models.Model):
	coureur = models.ForeignKey(Coureur, related_name='verloopcoureur_coureur', null=True)
	race = models.ForeignKey(Race, related_name='verloopcoureur_race', null=True)
	start_waarde = models.IntegerField(max_length=10, null=True)
	eind_waarde = models.IntegerField(max_length=10, null=True)
	
	objects = VerloopCoureursManager()
	

class VerloopTeamsManager(models.Manager):
	def create_verloop_team(self, team, race, start_waarde, eind_waarde):
		verloop_team = self.create(team=team,
				      race=race,
				      start_waarde=start_waarde,
				      eind_waarde=eind_waarde)
		return verloop_team

class VerloopTeams(models.Model):
	team = models.ForeignKey(Team, related_name='verloopteam_team', null=True)
	race = models.ForeignKey(Race, related_name='verloopteam_race', null=True)
	start_waarde = models.IntegerField(max_length=10, null=True)
	eind_waarde = models.IntegerField(max_length=10, null=True)

	objects = VerloopTeamsManager()
	
class Trivia(models.Model):
	race = models.ForeignKey(Race)
	vraag = models.CharField(max_length=100)
	antwoordA = models.CharField(max_length=25)
	antwoordB = models.CharField(max_length=25)
	antwoordC = models.CharField(max_length=25)
	antwoordD = models.CharField(max_length=25)
	correct_antwoord = models.CharField(max_length=1, choices=(('A','A'), ('B','B'), ('C','C'), ('D','D')))


class TeamAdmin(admin.ModelAdmin):
    list_display = ['naam', 'waarde', 'beschrijving', 'teamId']
    list_filter = ['waarde']
    ordering = ['-waarde']

class CoureurAdmin(admin.ModelAdmin):
    list_display = ['naam', 'driverId','waarde', 'team', 'beschrijving']
    list_filter = ['team']
    ordering = ['-waarde']

class UitslagRaceAdmin(admin.ModelAdmin):
    list_display = ['race']
    ordering = ['race']

class ScoreTabelAdmin(admin.ModelAdmin):
	list_display = ['score_type', 'kwali_race', 'uitslag',  'punten']
	list_filter = ['score_type', 'kwali_race']
	ordering = ['score_type', 'kwali_race', 'uitslag']

class WaardeTabelAdmin(admin.ModelAdmin):
	list_display = ['uitslag', 'plus_waarde', 'waarde_type']
	list_filter = ['waarde_type']
	ordering = ['waarde_type', 'uitslag']

class RaceAdmin(admin.ModelAdmin):
	list_display = ['naam', 'start', 'circuitId', 'is_aankomende_race', 'geupdate']
	ordering = ['start']

class UitslagPerCoureurAdmin(admin.ModelAdmin):
	list_display = ['race', 'coureur', 'positie_race', 'positie_kwali', 'status', 'drivethrough']
	list_filter = ['race', 'coureur' ]
	ordering = ['race', 'positie_race' ]
	
class ManueleInputAdmin(admin.ModelAdmin):
	list_display = ['race', 'snelste_pitstop']
	
class DriveThroughAdmin(admin.ModelAdmin):
	list_display = ['race', 'coureur']

class TriviaAdmin(admin.ModelAdmin):
	list_display = ['vraag', 'antwoordA', 'antwoordB', 'antwoordC', 'antwoordD']
	ordering = ['id']

   
admin.site.register(Team, TeamAdmin)
admin.site.register(Coureur, CoureurAdmin)
admin.site.register(ScoreTabel, ScoreTabelAdmin)
admin.site.register(WaardeTabel, WaardeTabelAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(UitslagPerCoureur, UitslagPerCoureurAdmin)
admin.site.register(ManueleInput, ManueleInputAdmin)
admin.site.register(DriveThrough, DriveThroughAdmin)
admin.site.register(Trivia, TriviaAdmin)

