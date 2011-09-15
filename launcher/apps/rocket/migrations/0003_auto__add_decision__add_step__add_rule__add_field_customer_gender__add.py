# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Decision'
        db.create_table('rocket_decision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('step', self.gf('django.db.models.fields.related.ForeignKey')(related_name='decisions', to=orm['rocket.Step'])),
            ('rule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rocket.Rule'])),
            ('goto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rocket.Step'])),
            ('match_all', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('rocket', ['Decision'])

        # Adding model 'Step'
        db.create_table('rocket_step', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sort', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(related_name='steps', to=orm['rocket.Campaign'])),
        ))
        db.send_create_signal('rocket', ['Step'])

        # Adding model 'Rule'
        db.create_table('rocket_rule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('behavior', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('rocket', ['Rule'])

        # Adding field 'Customer.gender'
        db.add_column('rocket_customer', 'gender', self.gf('django.db.models.fields.CharField')(default='U', max_length=1, db_index=True), keep_default=False)

        # Adding field 'Customer.age'
        db.add_column('rocket_customer', 'age', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # Adding index on 'Customer', fields ['email']
        db.create_index('rocket_customer', ['email'])

        # Adding index on 'Customer', fields ['uid']
        db.create_index('rocket_customer', ['uid'])


    def backwards(self, orm):
        
        # Removing index on 'Customer', fields ['uid']
        db.delete_index('rocket_customer', ['uid'])

        # Removing index on 'Customer', fields ['email']
        db.delete_index('rocket_customer', ['email'])

        # Deleting model 'Decision'
        db.delete_table('rocket_decision')

        # Deleting model 'Step'
        db.delete_table('rocket_step')

        # Deleting model 'Rule'
        db.delete_table('rocket_rule')

        # Deleting field 'Customer.gender'
        db.delete_column('rocket_customer', 'gender')

        # Deleting field 'Customer.age'
        db.delete_column('rocket_customer', 'age')


    models = {
        'rocket.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'begins': ('django.db.models.fields.DateTimeField', [], {}),
            'ends': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'campaigns'", 'to': "orm['rocket.Product']"})
        },
        'rocket.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rocket.customer': {
            'Meta': {'object_name': 'Customer'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '1', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'rocket.decision': {
            'Meta': {'object_name': 'Decision'},
            'goto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rocket.Step']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match_all': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rocket.Rule']"}),
            'step': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'decisions'", 'to': "orm['rocket.Step']"})
        },
        'rocket.product': {
            'Meta': {'object_name': 'Product'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rocket.rule': {
            'Meta': {'object_name': 'Rule'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'behavior': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rocket.step': {
            'Meta': {'object_name': 'Step'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'steps'", 'to': "orm['rocket.Campaign']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sort': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['rocket']
