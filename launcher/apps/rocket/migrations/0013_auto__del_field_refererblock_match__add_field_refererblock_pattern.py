# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'RefererBlock.match'
        db.delete_column('rocket_refererblock', 'match')

        # Adding field 'RefererBlock.pattern'
        db.add_column('rocket_refererblock', 'pattern', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'RefererBlock.match'
        db.add_column('rocket_refererblock', 'match', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Deleting field 'RefererBlock.pattern'
        db.delete_column('rocket_refererblock', 'pattern')


    models = {
        'rocket.brand': {
            'Meta': {'object_name': 'Brand'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rocket.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rocket.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'begins': ('django.db.models.fields.DateTimeField', [], {}),
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'campaigns'", 'null': 'True', 'blank': 'True', 'to': "orm['rocket.Brand']"}),
            'ends': ('django.db.models.fields.DateTimeField', [], {}),
            'google_analytics_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_units': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'rocket.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rocket.customer': {
            'Meta': {'object_name': 'Customer'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rocket.Campaign']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '1', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'meta': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'timezone': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'uid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'rocket.decision': {
            'Meta': {'object_name': 'Decision'},
            'goto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rocket.Step']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match_all': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rules': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'sort': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'step': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'decisions'", 'to': "orm['rocket.Step']"})
        },
        'rocket.refererblock': {
            'Meta': {'object_name': 'RefererBlock'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rocket.Campaign']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pattern': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rocket.session': {
            'Meta': {'object_name': 'Session'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rocket.Campaign']", 'null': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rocket.Customer']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_step': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['rocket.Step']", 'null': 'True', 'blank': 'True'})
        },
        'rocket.step': {
            'Meta': {'object_name': 'Step'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'steps'", 'to': "orm['rocket.Campaign']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sort': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'templates': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rocket']
