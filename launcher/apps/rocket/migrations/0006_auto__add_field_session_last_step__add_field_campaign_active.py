# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Session.last_step'
        db.add_column('rocket_session', 'last_step', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['rocket.Step'], null=True, blank=True), keep_default=False)

        # Adding field 'Campaign.active'
        db.add_column('rocket_campaign', 'active', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Session.last_step'
        db.delete_column('rocket_session', 'last_step_id')

        # Deleting field 'Campaign.active'
        db.delete_column('rocket_campaign', 'active')


    models = {
        'rocket.brand': {
            'Meta': {'object_name': 'Brand'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rocket.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'begins': ('django.db.models.fields.DateTimeField', [], {}),
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'campaigns'", 'to': "orm['rocket.Brand']"}),
            'ends': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'rocket.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_units': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
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
            'rules': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'step': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'decisions'", 'to': "orm['rocket.Step']"})
        },
        'rocket.refererblock': {
            'Meta': {'object_name': 'RefererBlock'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rocket.Campaign']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rocket.session': {
            'Meta': {'object_name': 'Session'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rocket.Customer']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_step': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['rocket.Step']", 'null': 'True', 'blank': 'True'})
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
