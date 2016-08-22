# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmserver', '0004_remove_list_pool_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListInfoLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('list_name', models.CharField(max_length=100, null=True, verbose_name='\u6e05\u5355\u540d', blank=True)),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='ip', blank=True)),
                ('col', models.CharField(max_length=100, null=True, verbose_name='\u53d8\u5316\u5b57\u6bb5', blank=True)),
                ('val_from', models.CharField(max_length=100, null=True, verbose_name='\u66f4\u65b0\u524d', blank=True)),
                ('val_to', models.CharField(max_length=100, null=True, verbose_name='\u66f4\u65b0\u540e', blank=True)),
                ('flag', models.CharField(max_length=100, null=True, verbose_name='\u589e\u5220\u6807\u8bb0', blank=True)),
                ('action_time', models.DateTimeField(null=True, verbose_name='\u53d8\u66f4\u65f6\u95f4', blank=True)),
                ('vm_ins', models.ForeignKey(verbose_name='vm\u5b9e\u4f8b', to_field='instance_uuid', blank=True, to='vmserver.List', null=True)),
            ],
            options={
                'verbose_name': 'vm\u4fe1\u606f\u53d8\u52a8\u65e5\u5fd7\u5e93',
                'verbose_name_plural': 'vm\u4fe1\u606f\u53d8\u52a8\u65e5\u5fd7\u5e93',
            },
        ),
    ]
