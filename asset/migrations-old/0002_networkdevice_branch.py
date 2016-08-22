# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkdevice',
            name='branch',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x88\x90\xe5\x91\x98\xe4\xbc\x81\xe4\xb8\x9a', blank=True),
        ),
    ]
