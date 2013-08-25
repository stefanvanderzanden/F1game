 #!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.forms.util import ErrorList
from django.contrib.auth.models import User
import time
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets
from django.utils.safestring import mark_safe


from users.models import *
from game.models import Trivia

class CreateUserForm(forms.Form):	
	GENDER = (
		('M', 'Man'),
		('V', 'Vrouw'),
	)
	voornaam = forms.CharField(max_length=100)
	tussenvoegsel = forms.CharField(max_length=50, required=False) 
	achternaam = forms.CharField(max_length=75)
	managernaam = forms.CharField(max_length=100)
	geslacht = forms.ChoiceField(choices=GENDER)
	email = forms.EmailField()
	wachtwoord = forms.CharField(widget=forms.PasswordInput())
	herhaal_wachtwoord = forms.CharField(widget=forms.PasswordInput())


class MijnTeamForm(forms.ModelForm):
	trivia = Trivia.objects.get(race__is_aankomende_race=True)
	antwoordA = trivia.antwoordA
	antwoordB = trivia.antwoordB
	antwoordC = trivia.antwoordC
	antwoordD = trivia.antwoordD
	
	trivia_antwoord = forms.ChoiceField(choices=(
		('A', antwoordA),
		('B', antwoordB),
		('C', antwoordC),
		('D', antwoordD)), widget=forms.RadioSelect)

	class Meta:
		model = MijnTeam
		exclude = ['userprofile']
		
	def __init__(self, user, *args, **kwargs):
		super(MijnTeamForm, self).__init__(*args, **kwargs)
		self.user = user
		'''
		Op volgorde zetten van waardes
		'''
		self.fields['coureur1'].queryset=Coureur.objects.all().order_by('-waarde')
		self.fields['coureur2'].queryset=Coureur.objects.all().order_by('-waarde')
		self.fields['team1'].queryset=Team.objects.all().order_by('-waarde')
		self.fields['team2'].queryset=Team.objects.all().order_by('-waarde')
		
		'''
		Zorgen dat het label in de dropdown menu's goed zijn.
		'''
		self.fields['coureur1'].label_from_instance = lambda obj: obj.naam + ' (' + u'€' + ' {0:,}'.format(obj.waarde).replace(',','.') + ')'
		self.fields['coureur2'].label_from_instance = lambda obj: obj.naam + ' (' + u'€' + ' {0:,}'.format(obj.waarde).replace(',','.') + ')'
		self.fields['team1'].label_from_instance = lambda obj: obj.naam + ' (' + u'€' + ' {0:,}'.format(obj.waarde).replace(',','.') + ')'
		self.fields['team2'].label_from_instance = lambda obj: obj.naam + ' (' + u'€' + ' {0:,}'.format(obj.waarde).replace(',','.') + ')'
				

	def clean(self):
		coureur1 = self.cleaned_data.get('coureur1')
		coureur2 = self.cleaned_data.get('coureur2')
		team1 = self.cleaned_data.get('team1')
		team2 = self.cleaned_data.get('team2')
		team_coureur1 = Team.objects.get(coureur=coureur1)
		team_coureur2 = Team.objects.get(coureur=coureur2)
		coureur1_waarde = Coureur.objects.get(pk=coureur1.id).waarde
		coureur2_waarde = Coureur.objects.get(pk=coureur2.id).waarde
		team1_waarde = Team.objects.get(pk=team1.id).waarde
		team2_waarde = Team.objects.get(pk=team2.id).waarde
		
		budget = UserProfile.objects.get(user=self.user).budget

		error_messages = []
		
		if coureur1 == coureur2:		
			error_messages.append('Coureurs kunnen niet gelijk zijn aan elkaar')
		
		if team1 == team2:

			error_messages.append('De teams kunnen niet gelijk zijn')

		if team_coureur1 == team1 or team_coureur1 == team2 or team_coureur2 == team1 or team_coureur2 == team2:
			error_messages.append('Gekozen coureurs mogen niet uit een gekozen team komen')
				
		if (coureur1_waarde + coureur2_waarde + team1_waarde + team2_waarde) > budget:
			error_messages.append('Niet genoeg budget')
		
		if len(error_messages):
			raise forms.ValidationError(error_messages)		


		return self.cleaned_data			

