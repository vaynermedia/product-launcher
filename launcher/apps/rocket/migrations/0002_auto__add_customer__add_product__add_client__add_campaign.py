# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Customer'
        db.create_table('rocket_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('uid', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('rocket', ['Customer'])

        # Adding model 'Product'
        db.create_table('rocket_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('rocket', ['Product'])

        # Adding model 'Client'
        db.create_table('rocket_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('rocket', ['Client'])

        # Adding model 'Campaign'
        db.create_table('rocket_campaign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rocket.Product'])),
            ('begins', self.gf('django.db.models.fields.DateTimeField')()),
            ('ends', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('rocket', ['Campaign'])


    def backwards(self, orm):
        
        # Deleting model 'Customer'
        db.delete_table('rocket_customer')

        # Deleting model 'Product'
        db.delete_table('rocket_product')

        # Deleting model 'Client'
        db.delete_table('rocket_client')

        # Deleting model 'Campaign'
        db.delete_table('rocket_campaign')


    models = {
        'rocket.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'begins': ('django.db.models.fields.DateTimeField', [], {}),
            'ends': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rocket.Product']"})
        },
        'rocket.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rocket.customer': {
            'Meta': {'object_name': 'Customer'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uid': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'rocket.product': {
            'Meta': {'object_name': 'Product'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['rocket']
