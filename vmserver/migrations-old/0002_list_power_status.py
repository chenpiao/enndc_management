# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmserver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='power_status',
            field=models.CharField(max_length=20, null=True, verbose_name='\u7535\u6e90\u72b6\u6001', blank=True),
        ),
    ]
