# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0014_auto_20160621_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='ownership',
            field=models.ForeignKey(related_name='ownership', verbose_name=b'\xe8\xb5\x84\xe4\xba\xa7\xe5\xbd\x92\xe5\xb1\x9e', to_field=b'name', blank=True, to='asset.IndustryGroup', null=True),
        ),
    ]
