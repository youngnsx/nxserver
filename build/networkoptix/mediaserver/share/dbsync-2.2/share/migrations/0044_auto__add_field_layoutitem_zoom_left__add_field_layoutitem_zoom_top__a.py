# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LayoutItem.zoom_left'
        db.add_column('vms_layoutitem', 'zoom_left',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'LayoutItem.zoom_top'
        db.add_column('vms_layoutitem', 'zoom_top',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'LayoutItem.zoom_right'
        db.add_column('vms_layoutitem', 'zoom_right',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'LayoutItem.zoom_bottom'
        db.add_column('vms_layoutitem', 'zoom_bottom',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'LayoutItem.zoom_target_uuid'
        db.add_column('vms_layoutitem', 'zoom_target_uuid',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LayoutItem.zoom_left'
        db.delete_column('vms_layoutitem', 'zoom_left')

        # Deleting field 'LayoutItem.zoom_top'
        db.delete_column('vms_layoutitem', 'zoom_top')

        # Deleting field 'LayoutItem.zoom_right'
        db.delete_column('vms_layoutitem', 'zoom_right')

        # Deleting field 'LayoutItem.zoom_bottom'
        db.delete_column('vms_layoutitem', 'zoom_bottom')

        # Deleting field 'LayoutItem.zoom_target_uuid'
        db.delete_column('vms_layoutitem', 'zoom_target_uuid')


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
        'vms.businessrule': {
            'Meta': {'object_name': 'BusinessRule'},
            'action_params': ('django.db.models.fields.CharField', [], {'max_length': '16384'}),
            'action_resources': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'action_resource'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['vms.Resource']"}),
            'action_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'aggregation_period': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '16384', 'null': 'True', 'blank': 'True'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'event_condition': ('django.db.models.fields.CharField', [], {'max_length': '16384'}),
            'event_resources': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'event_resource'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['vms.Resource']"}),
            'event_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'event_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'schedule': ('django.db.models.fields.CharField', [], {'max_length': '16384', 'null': 'True', 'blank': 'True'})
        },
        'vms.camera': {
            'Meta': {'object_name': 'Camera', '_ormbases': ['vms.Resource']},
            'audio_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'firmware': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'group_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'group_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'manually_added': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
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
        'vms.kvpair': {
            'Meta': {'object_name': 'KvPair'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'resource': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vms.Resource']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'vms.layout': {
            'Meta': {'object_name': 'Layout', '_ormbases': ['vms.Resource']},
            'background_height': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'background_image_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'background_opacity': ('django.db.models.fields.IntegerField', [], {'default': '70'}),
            'background_width': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'cell_aspect_ratio': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'cell_spacing_height': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'cell_spacing_width': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vms.UserProfile']"}),
            'user_can_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'zoom_bottom': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'zoom_left': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'zoom_right': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'zoom_target_uuid': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'zoom_top': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        'vms.license': {
            'Meta': {'object_name': 'License'},
            'camera_count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'raw_license': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
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
            'auth_key': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'net_addr_list': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'panic_mode': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'reserve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'}),
            'streaming_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        },
        'vms.setting': {
            'Meta': {'object_name': 'Setting'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'vms.storage': {
            'Meta': {'object_name': 'Storage', '_ormbases': ['vms.Resource']},
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'}),
            'space_limit': ('django.db.models.fields.IntegerField', [], {}),
            'used_for_writing': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'vms.userprofile': {
            'Meta': {'object_name': 'UserProfile', '_ormbases': ['vms.Resource']},
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'}),
            'rights': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['vms']