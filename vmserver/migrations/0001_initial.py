# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-29 15:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0001_initial'),
        ('ops', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('born_time', models.DateTimeField(auto_created=True, default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('instance_uuid', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='UUID')),
                ('list_name', models.CharField(max_length=255, null=True, verbose_name='\u6e05\u5355\u4e3b\u673a\u540d')),
                ('hostname', models.CharField(max_length=255, null=True, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='IP\u5730\u5740')),
                ('template', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u662f\u5426\u6a21\u677f')),
                ('os', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('os_version', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c\u53f7')),
                ('total_hard_disk', models.IntegerField(blank=True, null=True, verbose_name='\u603b\u786c\u76d8\u5bb9\u91cf')),
                ('cpu', models.IntegerField(blank=True, null=True, verbose_name='CPU\u6838\u5fc3\u6570\u91cf')),
                ('mem', models.IntegerField(blank=True, null=True, verbose_name='\u5185\u5b58')),
                ('delivery_time', models.DateField(blank=True, max_length=20, null=True, verbose_name='\u8d44\u6e90\u4ea4\u4ed8\u65f6\u95f4')),
                ('delete_time', models.DateField(blank=True, max_length=20, null=True, verbose_name='\u8d44\u6e90\u5220\u9664\u65f6\u95f4')),
                ('tools_status', models.CharField(blank=True, max_length=20, null=True, verbose_name='tools\u72b6\u6001')),
                ('guest_status', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u72b6\u6001')),
                ('power_status', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u7535\u6e90\u72b6\u6001')),
                ('esxi_host', models.GenericIPAddressField(blank=True, null=True, verbose_name='esxi\u4e3b\u673aIP')),
                ('vc', models.GenericIPAddressField(blank=True, null=True, verbose_name='VCenterIP')),
                ('app_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5e94\u7528\u540d\u79f0')),
                ('app_role', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5e94\u7528\u89d2\u8272')),
                ('app_description', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5e94\u7528\u63cf\u8ff0')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='\u4e0a\u6b21\u4fee\u6539\u65f6\u95f4')),
                ('app_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ops.Contact', to_field='name', verbose_name='\u7ba1\u7406\u5458')),
                ('industry_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.IndustryGroup', to_field='name', verbose_name='\u5f52\u5c5e\u516c\u53f8')),
            ],
            options={
                'verbose_name': 'Vsphere\u5e73\u53f0\u865a\u62df\u673a',
                'verbose_name_plural': 'Vsphere\u5e73\u53f0\u865a\u62df\u673a',
            },
        ),
        migrations.CreateModel(
            name='ListInfoLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u6e05\u5355\u540d')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip')),
                ('col', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u53d8\u5316\u5b57\u6bb5')),
                ('val_from', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u66f4\u65b0\u524d')),
                ('val_to', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u66f4\u65b0\u540e')),
                ('flag', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u589e\u5220\u6807\u8bb0')),
                ('action_time', models.DateTimeField(blank=True, null=True, verbose_name='\u53d8\u66f4\u65f6\u95f4')),
                ('vm_ins', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vmserver.List', to_field='instance_uuid', verbose_name='vm\u5b9e\u4f8b')),
            ],
            options={
                'verbose_name': 'vm\u4fe1\u606f\u53d8\u52a8\u65e5\u5fd7\u5e93',
                'verbose_name_plural': 'vm\u4fe1\u606f\u53d8\u52a8\u65e5\u5fd7\u5e93',
            },
        ),
    ]
