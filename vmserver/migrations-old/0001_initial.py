# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0013_auto_20160520_1024'),
        ('ops', '0007_hostinfo_manage_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('born_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', auto_created=True)),
                ('instance_uuid', models.CharField(max_length=255, unique=True, null=True, verbose_name='UUID', blank=True)),
                ('list_name', models.CharField(max_length=255, null=True, verbose_name='\u6e05\u5355\u4e3b\u673a\u540d')),
                ('hostname', models.CharField(max_length=255, null=True, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='IP\u5730\u5740')),
                ('os', models.CharField(max_length=100, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf', blank=True)),
                ('os_version', models.CharField(max_length=100, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c\u53f7', blank=True)),
                ('pool_id', models.CharField(max_length=20, null=True, verbose_name='\u8d44\u6e90\u6c60', blank=True)),
                ('total_hard_disk', models.CharField(max_length=100, null=True, verbose_name='\u603b\u786c\u76d8\u5bb9\u91cf', blank=True)),
                ('cpu', models.IntegerField(null=True, verbose_name='CPU\u6838\u5fc3\u6570\u91cf', blank=True)),
                ('mem', models.CharField(max_length=5, null=True, verbose_name='\u5185\u5b58', blank=True)),
                ('delivery_time', models.DateField(max_length=20, null=True, verbose_name='\u8d44\u6e90\u4ea4\u4ed8\u65f6\u95f4', blank=True)),
                ('delete_time', models.DateField(max_length=20, null=True, verbose_name='\u8d44\u6e90\u5220\u9664\u65f6\u95f4', blank=True)),
                ('tools_status', models.CharField(max_length=20, null=True, verbose_name='tools\u72b6\u6001', blank=True)),
                ('guest_status', models.CharField(max_length=20, null=True, verbose_name='\u72b6\u6001', blank=True)),
                ('esxi_host', models.GenericIPAddressField(null=True, verbose_name='esxi\u4e3b\u673aIP', blank=True)),
                ('vc', models.GenericIPAddressField(null=True, verbose_name='VCenterIP', blank=True)),
                ('app_name', models.CharField(max_length=100, null=True, verbose_name='\u5e94\u7528\u540d\u79f0', blank=True)),
                ('app_role', models.CharField(max_length=100, null=True, verbose_name='\u5e94\u7528\u89d2\u8272', blank=True)),
                ('app_description', models.CharField(max_length=100, null=True, verbose_name='\u5e94\u7528\u63cf\u8ff0', blank=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4e0a\u6b21\u4fee\u6539\u65f6\u95f4', null=True)),
                ('app_admin', models.ForeignKey(verbose_name='\u7ba1\u7406\u5458', to_field='name', blank=True, to='ops.Contact', null=True)),
                ('industry_group', models.ForeignKey(verbose_name='\u5f52\u5c5e\u516c\u53f8', to_field='name', blank=True, to='asset.IndustryGroup', null=True)),
            ],
            options={
                'verbose_name': 'Vsphere\u5e73\u53f0\u865a\u62df\u673a',
                'verbose_name_plural': 'Vsphere\u5e73\u53f0\u865a\u62df\u673a',
            },
        ),
    ]
