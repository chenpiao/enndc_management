# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0007_auto_20160512_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='sn',
            field=models.CharField(max_length=50, unique=True, null=True, verbose_name=b'SN\xe5\x8f\xb7', blank=True),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='sn',
            field=models.CharField(max_length=50, unique=True, null=True, verbose_name=b'SN\xe5\x8f\xb7', blank=True),
        ),
        migrations.AlterField(
            model_name='tape',
            name='sn',
            field=models.CharField(max_length=50, unique=True, null=True, verbose_name='SN\u53f7', blank=True),
        ),
    ]
