# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ops', '0005_auto_20160418_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vmserver',
            name='industry_groupName',
            field=models.ForeignKey(verbose_name=b'\xe8\xae\xa1\xe8\xb4\xb9\xe7\xbb\x84', to_field=b'name', to='asset.IndustryGroup', null=True),
        ),
    ]
