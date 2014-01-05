# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Utilisateur'
        db.create_table(u'stream_utilisateur', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('profession', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lieu', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'stream', ['Utilisateur'])

        # Adding model 'Message'
        db.create_table(u'stream_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('auteur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stream.Utilisateur'])),
            ('texte', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'stream', ['Message'])

        # Adding model 'Filtre'
        db.create_table(u'stream_filtre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lieu', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('profession', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'stream', ['Filtre'])


    def backwards(self, orm):
        # Deleting model 'Utilisateur'
        db.delete_table(u'stream_utilisateur')

        # Deleting model 'Message'
        db.delete_table(u'stream_message')

        # Deleting model 'Filtre'
        db.delete_table(u'stream_filtre')


    models = {
        u'stream.filtre': {
            'Meta': {'object_name': 'Filtre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'stream.message': {
            'Meta': {'object_name': 'Message'},
            'auteur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stream.Utilisateur']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texte': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'stream.utilisateur': {
            'Meta': {'object_name': 'Utilisateur'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['stream']