# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0013_auto_20160520_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='maintenance_group_name',
            field=models.ForeignKey(related_name='m_group', verbose_name=b'\xe7\xbb\xb4\xe4\xbf\x9d\xe5\x8d\x95\xe4\xbd\x8d', to_field=b'maintenance_group', to='asset.Maintenance'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_group',
            field=models.CharField(max_length=100, unique=True, null=True, verbose_name='\u7ef4\u4fdd\u5355\u4f4d\u540d\u79f0'),
        ),
    ]
