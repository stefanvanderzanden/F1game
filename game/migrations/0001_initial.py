# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table('game_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('waarde', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('beschrijving', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('teamId', self.gf('django.db.models.fields.CharField')(default='id', max_length=20)),
        ))
        db.send_create_signal('game', ['Team'])

        # Adding model 'Coureur'
        db.create_table('game_coureur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('waarde', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Team'])),
            ('beschrijving', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('driverId', self.gf('django.db.models.fields.CharField')(default='id', max_length=20)),
        ))
        db.send_create_signal('game', ['Coureur'])

        # Adding model 'Race'
        db.create_table('game_race', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(max_length=130)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('circuitId', self.gf('django.db.models.fields.CharField')(default='id', max_length=20)),
            ('circuitNr', self.gf('django.db.models.fields.CharField')(default='1', max_length=20)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('beschrijving', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('geupdate', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('game', ['Race'])

        # Adding model 'ScoreTabel'
        db.create_table('game_scoretabel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('score_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('kwali_race', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('uitslag', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('punten', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
        ))
        db.send_create_signal('game', ['ScoreTabel'])

        # Adding model 'WaardeTabel'
        db.create_table('game_waardetabel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('waarde_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('uitslag', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('plus_waarde', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
        ))
        db.send_create_signal('game', ['WaardeTabel'])

        # Adding model 'UitslagPerCoureur'
        db.create_table('game_uitslagpercoureur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coureur', self.gf('django.db.models.fields.related.ForeignKey')(related_name='uitslagcoureur_coureur', to=orm['game.Coureur'])),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(related_name='uitslagcoureur_race', to=orm['game.Race'])),
            ('positie_kwali', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('positie_race', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('drivethrough', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('punten_kwali_coureur', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4)),
            ('punten_race_coureur', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4)),
            ('punten_kwali_team', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4)),
            ('punten_race_team', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4)),
        ))
        db.send_create_signal('game', ['UitslagPerCoureur'])

        # Adding unique constraint on 'UitslagPerCoureur', fields ['coureur', 'race']
        db.create_unique('game_uitslagpercoureur', ['coureur_id', 'race_id'])

        # Adding model 'SnelstePerRace'
        db.create_table('game_snelsteperrace', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Race'])),
            ('snelste_coureur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Coureur'])),
            ('snelste_pitstop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Team'])),
        ))
        db.send_create_signal('game', ['SnelstePerRace'])

        # Adding model 'VerloopCoureurs'
        db.create_table('game_verloopcoureurs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coureur', self.gf('django.db.models.fields.related.ForeignKey')(related_name='verloopcoureur_coureur', null=True, to=orm['game.Coureur'])),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(related_name='verloopcoureur_race', null=True, to=orm['game.Race'])),
            ('start_waarde', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True)),
            ('eind_waarde', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True)),
        ))
        db.send_create_signal('game', ['VerloopCoureurs'])

        # Adding model 'VerloopTeams'
        db.create_table('game_verloopteams', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='verloopteam_team', null=True, to=orm['game.Team'])),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(related_name='verloopteam_race', null=True, to=orm['game.Race'])),
            ('start_waarde', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True)),
            ('eind_waarde', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True)),
        ))
        db.send_create_signal('game', ['VerloopTeams'])

        # Adding model 'Trivia'
        db.create_table('game_trivia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Race'])),
            ('vraag', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('antwoordA', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('antwoordB', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('antwoordC', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('antwoordD', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('correct_antwoord', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('game', ['Trivia'])


    def backwards(self, orm):
        # Removing unique constraint on 'UitslagPerCoureur', fields ['coureur', 'race']
        db.delete_unique('game_uitslagpercoureur', ['coureur_id', 'race_id'])

        # Deleting model 'Team'
        db.delete_table('game_team')

        # Deleting model 'Coureur'
        db.delete_table('game_coureur')

        # Deleting model 'Race'
        db.delete_table('game_race')

        # Deleting model 'ScoreTabel'
        db.delete_table('game_scoretabel')

        # Deleting model 'WaardeTabel'
        db.delete_table('game_waardetabel')

        # Deleting model 'UitslagPerCoureur'
        db.delete_table('game_uitslagpercoureur')

        # Deleting model 'SnelstePerRace'
        db.delete_table('game_snelsteperrace')

        # Deleting model 'VerloopCoureurs'
        db.delete_table('game_verloopcoureurs')

        # Deleting model 'VerloopTeams'
        db.delete_table('game_verloopteams')

        # Deleting model 'Trivia'
        db.delete_table('game_trivia')


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
        'game.race': {
            'Meta': {'object_name': 'Race'},
            'beschrijving': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'circuitId': ('django.db.models.fields.CharField', [], {'default': "'id'", 'max_length': '20'}),
            'circuitNr': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '20'}),
            'geupdate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        'game.snelsteperrace': {
            'Meta': {'object_name': 'SnelstePerRace'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Race']"}),
            'snelste_coureur': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Coureur']"}),
            'snelste_pitstop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Team']"})
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