# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ScorePerRace.coureur1_punten_kwali'
        db.add_column('users_scoreperrace', 'coureur1_punten_kwali',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)

        # Adding field 'ScorePerRace.coureur1_punten_race'
        db.add_column('users_scoreperrace', 'coureur1_punten_race',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)

        # Adding field 'ScorePerRace.coureur2_punten_kwali'
        db.add_column('users_scoreperrace', 'coureur2_punten_kwali',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)

        # Adding field 'ScorePerRace.coureur2_punten_race'
        db.add_column('users_scoreperrace', 'coureur2_punten_race',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)

        # Adding field 'ScorePerRace.team1_coureur1_punten_kwali'
        db.add_column('users_scoreperrace', 'team1_coureur1_punten_kwali',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)

        # Adding field 'ScorePerRace.team1_coureur1_punten_race'
        db.add_column('users_scoreperrace', 'team1_coureur1_punten_race',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)

        # Adding field 'ScorePerRace.team1_coureur2_punten_kwali'
        db.add_column('users_scoreperrace', 'team1_coureur2_punten_kwali',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)

        # Adding field 'ScorePerRace.team1_coureur2_punten_race'
        db.add_column('users_scoreperrace', 'team1_coureur2_punten_race',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)

        # Adding field 'ScorePerRace.team2_coureur1_punten_kwali'
        db.add_column('users_scoreperrace', 'team2_coureur1_punten_kwali',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)

        # Adding field 'ScorePerRace.team2_coureur1_punten_race'
        db.add_column('users_scoreperrace', 'team2_coureur1_punten_race',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)

        # Adding field 'ScorePerRace.team2_coureur2_punten_kwali'
        db.add_column('users_scoreperrace', 'team2_coureur2_punten_kwali',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)

        # Adding field 'ScorePerRace.team2_coureur2_punten_race'
        db.add_column('users_scoreperrace', 'team2_coureur2_punten_race',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ScorePerRace.coureur1_punten_kwali'
        db.delete_column('users_scoreperrace', 'coureur1_punten_kwali')

        # Deleting field 'ScorePerRace.coureur1_punten_race'
        db.delete_column('users_scoreperrace', 'coureur1_punten_race')

        # Deleting field 'ScorePerRace.coureur2_punten_kwali'
        db.delete_column('users_scoreperrace', 'coureur2_punten_kwali')

        # Deleting field 'ScorePerRace.coureur2_punten_race'
        db.delete_column('users_scoreperrace', 'coureur2_punten_race')

        # Deleting field 'ScorePerRace.team1_coureur1_punten_kwali'
        db.delete_column('users_scoreperrace', 'team1_coureur1_punten_kwali')

        # Deleting field 'ScorePerRace.team1_coureur1_punten_race'
        db.delete_column('users_scoreperrace', 'team1_coureur1_punten_race')

        # Deleting field 'ScorePerRace.team1_coureur2_punten_kwali'
        db.delete_column('users_scoreperrace', 'team1_coureur2_punten_kwali')

        # Deleting field 'ScorePerRace.team1_coureur2_punten_race'
        db.delete_column('users_scoreperrace', 'team1_coureur2_punten_race')

        # Deleting field 'ScorePerRace.team2_coureur1_punten_kwali'
        db.delete_column('users_scoreperrace', 'team2_coureur1_punten_kwali')

        # Deleting field 'ScorePerRace.team2_coureur1_punten_race'
        db.delete_column('users_scoreperrace', 'team2_coureur1_punten_race')

        # Deleting field 'ScorePerRace.team2_coureur2_punten_kwali'
        db.delete_column('users_scoreperrace', 'team2_coureur2_punten_kwali')

        # Deleting field 'ScorePerRace.team2_coureur2_punten_race'
        db.delete_column('users_scoreperrace', 'team2_coureur2_punten_race')


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
            'is_aankomende_race': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'coureur1_punten_kwali': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'coureur1_punten_race': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'coureur2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scoreperrace_coureur2'", 'null': 'True', 'to': "orm['game.Coureur']"}),
            'coureur2_punten_kwali': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'coureur2_punten_race': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oude_punten': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Race']"}),
            'snelste_coureur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scoreperrace_snelstecoureur'", 'null': 'True', 'to': "orm['game.Coureur']"}),
            'snelste_pitstop': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scoreperrace_snelstepitstop'", 'null': 'True', 'to': "orm['game.Team']"}),
            'team1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scoreperrace_team1'", 'null': 'True', 'to': "orm['game.Team']"}),
            'team1_coureur1_punten_kwali': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'team1_coureur1_punten_race': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'team1_coureur2_punten_kwali': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'team1_coureur2_punten_race': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'team2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scoreperrace_team2'", 'null': 'True', 'to': "orm['game.Team']"}),
            'team2_coureur1_punten_kwali': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'team2_coureur1_punten_race': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'team2_coureur2_punten_kwali': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'team2_coureur2_punten_race': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
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