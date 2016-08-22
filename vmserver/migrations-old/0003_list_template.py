# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmserver', '0002_list_power_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='template',
            field=models.CharField(max_length=20, null=True, verbose_name='\u662f\u5426\u6a21\u677f', blank=True),
        ),
    ]
