# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'DeviceXmlLoadTime'
        db.create_table('vms_devicexmlloadtime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('time', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('vms', ['DeviceXmlLoadTime'])

        # Adding model 'Manufacture'
        db.create_table('vms_manufacture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('vms', ['Manufacture'])

        # Adding model 'ResourceType'
        db.create_table('vms_resourcetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('manufacture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vms.Manufacture'], null=True, blank=True)),
        ))
        db.send_create_signal('vms', ['ResourceType'])

        # Adding M2M table for field parents on 'ResourceType'
        db.create_table('vms_resourcetype_parents', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_resourcetype', models.ForeignKey(orm['vms.resourcetype'], null=False)),
            ('to_resourcetype', models.ForeignKey(orm['vms.resourcetype'], null=False))
        ))
        db.create_unique('vms_resourcetype_parents', ['from_resourcetype_id', 'to_resourcetype_id'])

        # Adding model 'PropertyType'
        db.create_table('vms_propertytype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resource_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vms.ResourceType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('step', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('values', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('ui_values', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('default_value', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('netHelper', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('sub_group', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ui', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('readonly', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('vms', ['PropertyType'])

        # Adding model 'CameraType'
        db.create_table('vms_cameratype', (
            ('resourcetype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vms.ResourceType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('vms', ['CameraType'])

        # Adding model 'EventType'
        db.create_table('vms_eventtype', (
            ('resourcetype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vms.ResourceType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('vms', ['EventType'])

        # Adding model 'ActionType'
        db.create_table('vms_actiontype', (
            ('resourcetype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vms.ResourceType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('vms', ['ActionType'])

        # Adding model 'EventActionParamType'
        db.create_table('vms_eventactionparamtype', (
            ('resourcetype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vms.ResourceType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('vms', ['EventActionParamType'])

        # Adding model 'Resource'
        db.create_table('vms_resource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vms.Resource'], null=True, blank=True)),
            ('xtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vms.ResourceType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('vms', ['Resource'])

        # Adding model 'LocalResource'
        db.create_table('vms_localresource', (
            ('resource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vms.Resource'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('vms', ['LocalResource'])

        # Adding model 'UserProfile'
        db.create_table('vms_userprofile', (
            ('resource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vms.Resource'], unique=True, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('vms', ['UserProfile'])

        # Adding model 'Property'
        db.create_table('vms_property', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vms.Resource'])),
            ('property_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vms.PropertyType'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('vms', ['Property'])

        # Adding model 'NetworkDevice'
        db.create_table('vms_networkdevice', (
            ('resource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vms.Resource'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('vms', ['NetworkDevice'])

        # Adding model 'Camera'
        db.create_table('vms_camera', (
            ('networkdevice_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vms.NetworkDevice'], unique=True, primary_key=True)),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
        ))
        db.send_create_signal('vms', ['Camera'])

        # Adding model 'Server'
        db.create_table('vms_server', (
            ('resource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vms.Resource'], unique=True, primary_key=True)),
            ('guid', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('api_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('vms', ['Server'])

        # Adding model 'Storage'
        db.create_table('vms_storage', (
            ('resource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vms.Resource'], unique=True, primary_key=True)),
            ('space_limit', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('vms', ['Storage'])

        # Adding model 'ScheduleTask'
        db.create_table('vms_scheduletask', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vms.Camera'])),
            ('start_time', self.gf('django.db.models.fields.IntegerField')()),
            ('end_time', self.gf('django.db.models.fields.IntegerField')()),
            ('do_record_audio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('record_type', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('day_of_week', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('before_threshold', self.gf('django.db.models.fields.IntegerField')()),
            ('after_threshold', self.gf('django.db.models.fields.IntegerField')()),
            ('stream_quality', self.gf('django.db.models.fields.SmallIntegerField')(default=4)),
            ('fps', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('vms', ['ScheduleTask'])

        # Adding model 'Layout'
        db.create_table('vms_layout', (
            ('resource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vms.Resource'], unique=True, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vms.UserProfile'])),
        ))
        db.send_create_signal('vms', ['Layout'])

        # Adding model 'LayoutItem'
        db.create_table('vms_layoutitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('layout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vms.Layout'])),
            ('resource', self.gf('django.db.models.fields.related.ForeignKey')(related_name='layout_resource', to=orm['vms.Resource'])),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('flags', self.gf('django.db.models.fields.IntegerField')()),
            ('left', self.gf('django.db.models.fields.FloatField')()),
            ('top', self.gf('django.db.models.fields.FloatField')()),
            ('right', self.gf('django.db.models.fields.FloatField')()),
            ('bottom', self.gf('django.db.models.fields.FloatField')()),
            ('rotation', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('vms', ['LayoutItem'])


    def backwards(self, orm):
        
        # Deleting model 'DeviceXmlLoadTime'
        db.delete_table('vms_devicexmlloadtime')

        # Deleting model 'Manufacture'
        db.delete_table('vms_manufacture')

        # Deleting model 'ResourceType'
        db.delete_table('vms_resourcetype')

        # Removing M2M table for field parents on 'ResourceType'
        db.delete_table('vms_resourcetype_parents')

        # Deleting model 'PropertyType'
        db.delete_table('vms_propertytype')

        # Deleting model 'CameraType'
        db.delete_table('vms_cameratype')

        # Deleting model 'EventType'
        db.delete_table('vms_eventtype')

        # Deleting model 'ActionType'
        db.delete_table('vms_actiontype')

        # Deleting model 'EventActionParamType'
        db.delete_table('vms_eventactionparamtype')

        # Deleting model 'Resource'
        db.delete_table('vms_resource')

        # Deleting model 'LocalResource'
        db.delete_table('vms_localresource')

        # Deleting model 'UserProfile'
        db.delete_table('vms_userprofile')

        # Deleting model 'Property'
        db.delete_table('vms_property')

        # Deleting model 'NetworkDevice'
        db.delete_table('vms_networkdevice')

        # Deleting model 'Camera'
        db.delete_table('vms_camera')

        # Deleting model 'Server'
        db.delete_table('vms_server')

        # Deleting model 'Storage'
        db.delete_table('vms_storage')

        # Deleting model 'ScheduleTask'
        db.delete_table('vms_scheduletask')

        # Deleting model 'Layout'
        db.delete_table('vms_layout')

        # Deleting model 'LayoutItem'
        db.delete_table('vms_layoutitem')


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
            'Meta': {'object_name': 'Camera', '_ormbases': ['vms.NetworkDevice']},
            'login': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'networkdevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.NetworkDevice']", 'unique': 'True', 'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'})
        },
        'vms.cameratype': {
            'Meta': {'object_name': 'CameraType', '_ormbases': ['vms.ResourceType']},
            'resourcetype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.ResourceType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'vms.devicexmlloadtime': {
            'Meta': {'object_name': 'DeviceXmlLoadTime'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'time': ('django.db.models.fields.IntegerField', [], {})
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
        'vms.localresource': {
            'Meta': {'object_name': 'LocalResource', '_ormbases': ['vms.Resource']},
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'})
        },
        'vms.manufacture': {
            'Meta': {'object_name': 'Manufacture'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'vms.networkdevice': {
            'Meta': {'object_name': 'NetworkDevice', '_ormbases': ['vms.Resource']},
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vms.Resource']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
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
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'})
        },
        'vms.storage': {
            'Meta': {'object_name': 'Storage', '_ormbases': ['vms.Resource']},
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'}),
            'space_limit': ('django.db.models.fields.IntegerField', [], {})
        },
        'vms.userprofile': {
            'Meta': {'object_name': 'UserProfile', '_ormbases': ['vms.Resource']},
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vms.Resource']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['vms']
