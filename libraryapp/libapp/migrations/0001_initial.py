# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Books'
        db.create_table(u'libapp_books', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_of_pub', self.gf('django.db.models.fields.DateField')()),
            ('isbn_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('book_author', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('book_category', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('qty_in_lib', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('qty_available', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'libapp', ['Books'])

        # Adding model 'BookUserMap'
        db.create_table(u'libapp_bookusermap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['libapp.Books'])),
            ('issue_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2015, 2, 24, 0, 0))),
            ('return_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('days', self.gf('django.db.models.fields.IntegerField')(default=7)),
            ('fine', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('book_returned', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'libapp', ['BookUserMap'])


    def backwards(self, orm):
        # Deleting model 'Books'
        db.delete_table(u'libapp_books')

        # Deleting model 'BookUserMap'
        db.delete_table(u'libapp_bookusermap')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'libapp.books': {
            'Meta': {'object_name': 'Books'},
            'book_author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'book_category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'book_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_of_pub': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'qty_available': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'qty_in_lib': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'libapp.bookusermap': {
            'Meta': {'object_name': 'BookUserMap'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['libapp.Books']"}),
            'book_returned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'days': ('django.db.models.fields.IntegerField', [], {'default': '7'}),
            'fine': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2015, 2, 24, 0, 0)'}),
            'return_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['libapp']