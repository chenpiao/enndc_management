# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='appRole',
            new_name='app_role',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='Cluster',
            new_name='cluster',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='CPU',
            new_name='cpu',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='Domain',
            new_name='domain',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='HardDisk',
            new_name='hard_disk',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='IndustryGroupName',
            new_name='industry_groupName',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='Mem',
            new_name='mem',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='OS',
            new_name='os',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='OsVersion',
            new_name='os_version',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='TotalHardDisk',
            new_name='total_hard_disk',
        ),
    ]
