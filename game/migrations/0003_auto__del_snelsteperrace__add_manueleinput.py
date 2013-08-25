# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SnelstePerRace'
        db.delete_table('game_snelsteperrace')

        # Adding model 'ManueleInput'
        db.create_table('game_manueleinput', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Race'])),
            ('snelste_coureur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Coureur'], null=True)),
            ('snelste_pitstop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Team'])),
        ))
        db.send_create_signal('game', ['ManueleInput'])


    def backwards(self, orm):
        # Adding model 'SnelstePerRace'
        db.create_table('game_snelsteperrace', (
            ('snelste_pitstop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Team'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Race'])),
            ('snelste_coureur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Coureur'])),
        ))
        db.send_create_signal('game', ['SnelstePerRace'])

        # Deleting model 'ManueleInput'
        db.delete_table('game_manueleinput')


    models = {
        'game.coureur': {
            'Meta': {'object_name': 'Coureur'},
            'beschrijving': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'driverId': ('django.db.models.fields.CharField', [], {'default': "'id'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Team']"}),
            'waarde': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        'game.manueleinput': {
            'Meta': {'object_name': 'ManueleInput'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Race']"}),
            'snelste_coureur': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Coureur']", 'null': 'True'}),
            'snelste_pitstop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Team']"})
        },
        'game.race': {
            'Meta': {'object_name': 'Race'},
            'beschrijving': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'circuitId': ('django.db.models.fields.CharField', [], {'default': "'id'", 'max_length': '20'}),
            'circuitNr': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '20'}),
            'geupdate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_aankomende_race': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '130'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'game.scoretabel': {
            'Meta': {'object_name': 'ScoreTabel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kwali_race': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'punten': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'score_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'uitslag': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        'game.team': {
            'Meta': {'object_name': 'Team'},
            'beschrijving': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'teamId': ('django.db.models.fields.CharField', [], {'default': "'id'", 'max_length': '20'}),
            'waarde': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        'game.trivia': {
            'Meta': {'object_name': 'Trivia'},
            'antwoordA': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'antwoordB': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'antwoordC': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'antwoordD': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'correct_antwoord': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Race']"}),
            'vraag': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'game.uitslagpercoureur': {
            'Meta': {'unique_together': "(('coureur', 'race'),)", 'object_name': 'UitslagPerCoureur'},
            'coureur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uitslagcoureur_coureur'", 'to': "orm['game.Coureur']"}),
            'drivethrough': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'positie_kwali': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'positie_race': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'punten_kwali_coureur': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'punten_kwali_team': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'punten_race_coureur': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'punten_race_team': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uitslagcoureur_race'", 'to': "orm['game.Race']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'game.verloopcoureurs': {
            'Meta': {'object_name': 'VerloopCoureurs'},
            'coureur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'verloopcoureur_coureur'", 'null': 'True', 'to': "orm['game.Coureur']"}),
            'eind_waarde': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'verloopcoureur_race'", 'null': 'True', 'to': "orm['game.Race']"}),
            'start_waarde': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True'})
        },
        'game.verloopteams': {
            'Meta': {'object_name': 'VerloopTeams'},
            'eind_waarde': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'verloopteam_race'", 'null': 'True', 'to': "orm['game.Race']"}),
            'start_waarde': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'verloopteam_team'", 'null': 'True', 'to': "orm['game.Team']"})
        },
        'game.waardetabel': {
            'Meta': {'object_name': 'WaardeTabel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plus_waarde': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'uitslag': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'waarde_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['game']