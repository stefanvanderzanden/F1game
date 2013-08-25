from django import forms
from django.contrib.auth.models import User
import time
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets

from game.models import *

'''
class UitslagRaceForm(forms.ModelForm):

	class Meta:
		model = UitslagRace
		exclude = ['race', 'ingevoerd']
	
	def __init__(self, *args, **kwargs):
		super(UitslagRaceForm, self).__init__(*args, **kwargs)
		x = 1
		while x <= 22:
			field_kwali = 'nr_'+str(x)+'_kwali'
			field_race = 'nr_'+str(x)+'_race'
			self.fields[field_kwali].queryset=Coureur.objects.all().order_by('-waarde')
			self.fields[field_race].queryset=Coureur.objects.all().order_by('-waarde')
			x+=1
'''
