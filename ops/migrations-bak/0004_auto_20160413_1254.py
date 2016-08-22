# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0003_auto_20160330_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='hostname',
            field=models.CharField(max_length=255, verbose_name='\u7269\u7406\u4e3b\u673a\u540d', blank=True),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='type',
            field=models.CharField(blank=True, max_length=10, verbose_name='\u5e94\u7528\u670d\u52a1\u7c7b\u522b', choices=[('pro', '\u751f\u4ea7'), ('dev_test', '\u5f00\u53d1\u6d4b\u8bd5'), ('lib', '\u5b9e\u9a8c')]),
        ),
    ]
