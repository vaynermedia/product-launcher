# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Rule'
        db.delete_table('rocket_rule')

        # Adding model 'Session'
        db.create_table('rocket_session', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rocket.Customer'], null=True, blank=True)),
        ))
        db.send_create_signal('rocket', ['Session'])

        # Adding model 'RefererBlock'
        db.create_table('rocket_refererblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rocket.Campaign'])),
            ('match', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('rocket', ['RefererBlock'])

        # Deleting field 'Decision.rule'
        db.delete_column('rocket_decision', 'rule_id')

        # Adding field 'Decision.rules'
        db.add_column('rocket_decision', 'rules', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'Client.total_units'
        db.add_column('rocket_client', 'total_units', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Rule'
        db.create_table('rocket_rule', (
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('behavior', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('rocket', ['Rule'])

        # Deleting model 'Session'
        db.delete_table('rocket_session')

        # Deleting model 'RefererBlock'
        db.delete_table('rocket_refererblock')

        # User chose to not deal with backwards NULL issues for 'Decision.rule'
        raise RuntimeError("Cannot reverse this migration. 'Decision.rule' and its values cannot be restored.")

        # Deleting field 'Decision.rules'
        db.delete_column('rocket_decision', 'rules')

        # Deleting field 'Client.total_units'
        db.delete_column('rocket_client', 'total_units')


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
        'rocket.product': {
            'Meta': {'object_name': 'Product'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
