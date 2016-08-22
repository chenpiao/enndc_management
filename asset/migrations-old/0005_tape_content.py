# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_storagesparepart'),
    ]

    operations = [
        migrations.AddField(
            model_name='tape',
            name='content',
            field=models.CharField(max_length=200, null=True, verbose_name='\u6570\u636e\u5185\u5bb9', blank=True),
        ),
    ]
