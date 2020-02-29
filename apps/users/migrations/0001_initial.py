# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ScorePerRace'
        db.create_table('users_scoreperrace', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Race'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('coureur1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='scoreperrace_coureur1', null=True, to=orm['game.Coureur'])),
            ('coureur2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='scoreperrace_coureur2', null=True, to=orm['game.Coureur'])),
            ('team1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='scoreperrace_team1', null=True, to=orm['game.Team'])),
            ('team2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='scoreperrace_team2', null=True, to=orm['game.Team'])),
            ('trivia', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('snelste_coureur', self.gf('django.db.models.fields.related.ForeignKey')(related_name='scoreperrace_snelstecoureur', null=True, to=orm['game.Coureur'])),
            ('snelste_pitstop', self.gf('django.db.models.fields.related.ForeignKey')(related_name='scoreperrace_snelstepitstop', null=True, to=orm['game.Team'])),
            ('oude_punten', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4)),
            ('totaal_kwali', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('totaal_race', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('totaal', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
        ))
        db.send_create_signal('users', ['ScorePerRace'])

        # Adding model 'UserProfile'
        db.create_table('users_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('geslacht', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('tussenvoegsel', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('volledige_naam', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('volledige_achternaam', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('punten', self.gf('django.db.models.fields.IntegerField')(max_length=6, null=True, blank=True)),
            ('budget', self.gf('django.db.models.fields.IntegerField')(max_length=15, null=True, blank=True)),
            ('jokers', self.gf('django.db.models.fields.IntegerField')(max_length=1, null=True, blank=True)),
            ('kosten', self.gf('django.db.models.fields.IntegerField')(max_length=15, null=True, blank=True)),
            ('balans', self.gf('django.db.models.fields.IntegerField')(max_length=15, null=True, blank=True)),
        ))
        db.send_create_signal('users', ['UserProfile'])

        # Adding model 'MijnTeam'
        db.create_table('users_mijnteam', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userprofile', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.UserProfile'], unique=True)),
            ('coureur1', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mijnteam_coureur1', null=True, to=orm['game.Coureur'])),
            ('coureur2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mijnteam_coureur2', null=True, to=orm['game.Coureur'])),
            ('team1', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mijnteam_team1', null=True, to=orm['game.Team'])),
            ('team2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mijnteam_team2', null=True, to=orm['game.Team'])),
            ('joker_coureur1', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('joker_coureur2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('joker_team1', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('joker_team2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('snelste_coureur', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mijnteam_snelstecoureur', null=True, to=orm['game.Coureur'])),
            ('snelste_pitstop', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mijnteam_snelstepitstop', null=True, to=orm['game.Team'])),
            ('trivia_antwoord', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
        ))
        db.send_create_signal('users', ['MijnTeam'])


    def backwards(self, orm):
        # Deleting model 'ScorePerRace'
        db.delete_table('users_scoreperrace')

        # Deleting model 'UserProfile'
        db.delete_table('users_userprofile')

        # Deleting model 'MijnTeam'
        db.delete_table('users_mijnteam')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        'game.team': {
            'Meta': {'object_name': 'Team'},
            'beschrijving': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'teamId': ('django.db.models.fields.CharField', [], {'default': "'id'", 'max_length': '20'}),
            'waarde': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        'users.mijnteam': {
            'Meta': {'object_name': 'MijnTeam'},
            'coureur1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mijnteam_coureur1'", 'null': 'True', 'to': "orm['game.Coureur']"}),
            'coureur2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mijnteam_coureur2'", 'null': 'True', 'to': "orm['game.Coureur']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joker_coureur1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'joker_coureur2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'joker_team1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'joker_team2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'snelste_coureur': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mijnteam_snelstecoureur'", 'null': 'True', 'to': "orm['game.Coureur']"}),
            'snelste_pitstop': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mijnteam_snelstepitstop'", 'null': 'True', 'to': "orm['game.Team']"}),
            'team1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mijnteam_team1'", 'null': 'True', 'to': "orm['game.Team']"}),
            'team2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mijnteam_team2'", 'null': 'True', 'to': "orm['game.Team']"}),
            'trivia_antwoord': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'userprofile': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['users.UserProfile']", 'unique': 'True'})
        },
        'users.scoreperrace': {
            'Meta': {'object_name': 'ScorePerRace'},
            'coureur1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scoreperrace_coureur1'", 'null': 'True', 'to': "orm['game.Coureur']"}),
            'coureur2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scoreperrace_coureur2'", 'null': 'True', 'to': "orm['game.Coureur']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oude_punten': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Race']"}),
            'snelste_coureur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scoreperrace_snelstecoureur'", 'null': 'True', 'to': "orm['game.Coureur']"}),
            'snelste_pitstop': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scoreperrace_snelstepitstop'", 'null': 'True', 'to': "orm['game.Team']"}),
            'team1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scoreperrace_team1'", 'null': 'True', 'to': "orm['game.Team']"}),
            'team2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scoreperrace_team2'", 'null': 'True', 'to': "orm['game.Team']"}),
            'totaal': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'totaal_kwali': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'totaal_race': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'trivia': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'balans': ('django.db.models.fields.IntegerField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'budget': ('django.db.models.fields.IntegerField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'geslacht': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jokers': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'kosten': ('django.db.models.fields.IntegerField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'punten': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'tussenvoegsel': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'volledige_achternaam': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'volledige_naam': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['users']