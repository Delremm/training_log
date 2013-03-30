# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExerciseBodypart'
        db.create_table(u'log_app_exercisebodypart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bodypart_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'log_app', ['ExerciseBodypart'])

        # Adding model 'Exercise'
        db.create_table(u'log_app_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'log_app', ['Exercise'])

        # Adding M2M table for field bodypart on 'Exercise'
        db.create_table(u'log_app_exercise_bodypart', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exercise', models.ForeignKey(orm[u'log_app.exercise'], null=False)),
            ('exercisebodypart', models.ForeignKey(orm[u'log_app.exercisebodypart'], null=False))
        ))
        db.create_unique(u'log_app_exercise_bodypart', ['exercise_id', 'exercisebodypart_id'])

        # Adding model 'Workout'
        db.create_table(u'log_app_workout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 3, 22, 0, 0))),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='workouts', null=True, to=orm['auth.User'])),
            ('data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'log_app', ['Workout'])

        # Adding model 'Set'
        db.create_table(u'log_app_set', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['log_app.Exercise'])),
            ('data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sets', to=orm['log_app.Workout'])),
        ))
        db.send_create_signal(u'log_app', ['Set'])


    def backwards(self, orm):
        # Deleting model 'ExerciseBodypart'
        db.delete_table(u'log_app_exercisebodypart')

        # Deleting model 'Exercise'
        db.delete_table(u'log_app_exercise')

        # Removing M2M table for field bodypart on 'Exercise'
        db.delete_table('log_app_exercise_bodypart')

        # Deleting model 'Workout'
        db.delete_table(u'log_app_workout')

        # Deleting model 'Set'
        db.delete_table(u'log_app_set')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'log_app.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'bodypart': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'bodyparts'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['log_app.ExerciseBodypart']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'log_app.exercisebodypart': {
            'Meta': {'object_name': 'ExerciseBodypart'},
            'bodypart_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'log_app.set': {
            'Meta': {'object_name': 'Set'},
            'data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['log_app.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sets'", 'to': u"orm['log_app.Workout']"})
        },
        u'log_app.workout': {
            'Meta': {'object_name': 'Workout'},
            'data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 3, 22, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'workouts'", 'null': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['log_app']