# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ops', '0007_auto_20160418_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='OsVersion',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c\u53f7', choices=[('CentOS 5_x64', 'CentOS 5 (64\u4f4d)'), ('CentOS 5.8_x64', 'CentOS 5.8 (64\u4f4d)'), ('CentOS 7_x64', 'CentOS 7 (64\u4f4d)'), ('CentOS 6.5_x64', 'CentOS 6.5 (64\u4f4d)'), ('CentOS 6.7_x64', 'CentOS 6.7 (64\u4f4d)'), ('Linux\u5b9a\u5236', 'Linux\u5b9a\u5236'), ('Microsoft Windows 7', 'Microsoft Windows 7'), ('Microsoft Windows Server 2003', 'Microsoft Windows Server 2003'), ('Microsoft Windows Server 2008', 'Microsoft Windows Server 2008'), ('Microsoft Windows Server 2008 R2', 'Microsoft Windows Server 2008 R2'), ('Microsoft Windows XP Professional', 'Microsoft Windows XP Professional'), ('RHEL 6.5_x64', 'RHEL 6.5_x64'), ('RHEL 5.4_x64', 'RHEL 5.4_x64'), ('Ubuntu 12_x64', 'Ubuntu 12_x64'), ('Ubuntu Linux_x64', 'Ubuntu Linux_x64'), ('ESXI 5.0', 'ESXI 5.0'), ('ESXI 5.1 U3', 'ESXI 5.1 U3'), ('Ubuntu Linux_x64', 'Ubuntu Linux_x64')]),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='sn',
            field=models.ForeignKey(db_column=b'sn', verbose_name=b'SN\xe5\x8f\xb7', to_field=b'sn', to='asset.Host'),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='type',
            field=models.CharField(blank=True, max_length=10, verbose_name='\u5e94\u7528\u670d\u52a1\u7c7b\u522b', choices=[('\u751f\u4ea7', '\u751f\u4ea7'), ('\u5f00\u53d1\u6d4b\u8bd5', '\u5f00\u53d1\u6d4b\u8bd5'), ('\u5b9e\u9a8c', '\u5b9e\u9a8c')]),
        ),
        migrations.AlterField(
            model_name='vmserver',
            name='type',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u7c7b\u522b', choices=[('\u751f\u4ea7', '\u751f\u4ea7'), ('\u5f00\u53d1\u6d4b\u8bd5', '\u5f00\u53d1\u6d4b\u8bd5'), ('\u5b9e\u9a8c', '\u5b9e\u9a8c')]),
        ),
    ]
