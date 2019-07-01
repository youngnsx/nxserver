# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Camera.manually_added'
        db.add_column('vms_camera', 'manually_added',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Camera.manually_added'
        db.delete_column('vms_camera', 'manually_added')


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
        'vms.actiontype': {
            'Meta': {'object_name': 'ActionType', '_ormbases': ['vms.ResourceType']},
            'resourcetype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.ResourceType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'vms.camera': {
            'Meta': {'object_name': 'Camera', '_ormbases': ['vms.Resource']},
            'audio_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'manually_added': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'motion_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'physical_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'}),
            'schedule_disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'vms.cameraserveritem': {
            'Meta': {'object_name': 'CameraServerItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'physical_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'server_guid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {})
        },
        'vms.cameratype': {
            'Meta': {'object_name': 'CameraType', '_ormbases': ['vms.ResourceType']},
            'resourcetype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.ResourceType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'vms.eventactionparamtype': {
            'Meta': {'object_name': 'EventActionParamType', '_ormbases': ['vms.ResourceType']},
            'resourcetype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.ResourceType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'vms.eventtype': {
            'Meta': {'object_name': 'EventType', '_ormbases': ['vms.ResourceType']},
            'resourcetype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.ResourceType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'vms.layout': {
            'Meta': {'object_name': 'Layout', '_ormbases': ['vms.Resource']},
            'cell_aspect_ratio': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'cell_spacing_height': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'cell_spacing_width': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vms.UserProfile']"})
        },
        'vms.layoutitem': {
            'Meta': {'object_name': 'LayoutItem'},
            'bottom': ('django.db.models.fields.FloatField', [], {}),
            'flags': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vms.Layout']"}),
            'left': ('django.db.models.fields.FloatField', [], {}),
            'resource': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'layout_resource'", 'to': "orm['vms.Resource']"}),
            'right': ('django.db.models.fields.FloatField', [], {}),
            'rotation': ('django.db.models.fields.FloatField', [], {}),
            'top': ('django.db.models.fields.FloatField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'vms.license': {
            'Meta': {'object_name': 'License'},
            'camera_count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'vms.localresource': {
            'Meta': {'object_name': 'LocalResource', '_ormbases': ['vms.Resource']},
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'})
        },
        'vms.manufacture': {
            'Meta': {'object_name': 'Manufacture'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'vms.property': {
            'Meta': {'object_name': 'Property'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'property_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vms.PropertyType']"}),
            'resource': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vms.Resource']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'vms.propertytype': {
            'Meta': {'object_name': 'PropertyType'},
            'default_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'netHelper': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'readonly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resource_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vms.ResourceType']"}),
            'step': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sub_group': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'ui': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ui_values': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'values': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'vms.resource': {
            'Meta': {'object_name': 'Resource'},
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vms.Resource']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'xtype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vms.ResourceType']"})
        },
        'vms.resourcetype': {
            'Meta': {'object_name': 'ResourceType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vms.Manufacture']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['vms.ResourceType']", 'null': 'True', 'blank': 'True'})
        },
        'vms.scheduletask': {
            'Meta': {'object_name': 'ScheduleTask'},
            'after_threshold': ('django.db.models.fields.IntegerField', [], {}),
            'before_threshold': ('django.db.models.fields.IntegerField', [], {}),
            'day_of_week': ('django.db.models.fields.SmallIntegerField', [], {}),
            'do_record_audio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_time': ('django.db.models.fields.IntegerField', [], {}),
            'fps': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vms.Camera']"}),
            'start_time': ('django.db.models.fields.IntegerField', [], {}),
            'stream_quality': ('django.db.models.fields.SmallIntegerField', [], {'default': '4'})
        },
        'vms.server': {
            'Meta': {'object_name': 'Server', '_ormbases': ['vms.Resource']},
            'api_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'net_addr_list': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'panic_mode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reserve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'}),
            'streaming_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'vms.storage': {
            'Meta': {'object_name': 'Storage', '_ormbases': ['vms.Resource']},
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'}),
            'space_limit': ('django.db.models.fields.IntegerField', [], {})
        },
        'vms.userprofile': {
            'Meta': {'object_name': 'UserProfile', '_ormbases': ['vms.Resource']},
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'}),
            'rights': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['vms']