# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20160428_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageSparePart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=50, unique=True, null=True, verbose_name=b'\xe5\xa4\x87\xe4\xbb\xb6SN', blank=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7', choices=[('\u5185\u5b58', '\u5185\u5b58'), ('\u786c\u76d8', '\u786c\u76d8'), ('\u63a7\u5236\u5668', '\u63a7\u5236\u5668'), ('\u7535\u6e90\u6a21\u5757', '\u7535\u6e90\u6a21\u5757')])),
                ('vendor', models.CharField(max_length=50, null=True, verbose_name=b'\xe7\x94\x9f\xe4\xba\xa7\xe5\x8e\x82\xe5\x95\x86', blank=True)),
                ('capacity', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xae\xb9\xe9\x87\x8fG', blank=True)),
                ('host', models.ForeignKey(verbose_name=b'\xe5\xad\x98\xe5\x82\xa8\xe5\xa4\x87\xe4\xbb\xb6', blank=True, to='asset.Storage', null=True)),
            ],
            options={
                'verbose_name': '\u5b58\u50a8\u5907\u4ef6',
                'verbose_name_plural': '\u5b58\u50a8\u5907\u4ef6',
            },
        ),
    ]
