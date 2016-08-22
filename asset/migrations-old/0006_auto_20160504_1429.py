# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0005_tape_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='tape',
            name='host',
            field=models.ForeignKey(verbose_name=b'\xe6\x8c\x82\xe8\xbd\xbd\xe5\xad\x98\xe5\x82\xa8', to_field=b'sn', blank=True, to='asset.Storage', null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='cabinet',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9f\x9c\xe5\x8f\xb7', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (11028, '11028'), (11029, '11029'), (11030, '11030'), (11031, '11031'), (1204, '1204'), (1205, '1205'), (1206, '1206')]),
        ),
        migrations.AlterField(
            model_name='host',
            name='zone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9f\x9c\xe5\x8c\xba\xe5\x9f\x9f', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('101', '101'), ('109', '109')]),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='cabinet',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9f\x9c\xe5\x8f\xb7', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (11028, '11028'), (11029, '11029'), (11030, '11030'), (11031, '11031'), (1204, '1204'), (1205, '1205'), (1206, '1206')]),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='type',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe7\xb1\xbb\xe5\x9e\x8b', choices=[('\u4ea4\u6362\u673a', '\u4ea4\u6362\u673a'), ('\u9632\u706b\u5899', '\u9632\u706b\u5899'), ('\u8def\u7531\u5668', '\u8def\u7531\u5668'), ('\u65e0\u7ebfAP', '\u65e0\u7ebfAP'), ('\u5176\u5b83', '\u5176\u5b83')]),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='zone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9f\x9c\xe5\x8c\xba\xe5\x9f\x9f', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('101', '101'), ('109', '109')]),
        ),
        migrations.AlterField(
            model_name='storage',
            name='cabinet',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u673a\u67dc\u53f7', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (11028, '11028'), (11029, '11029'), (11030, '11030'), (11031, '11031'), (1204, '1204'), (1205, '1205'), (1206, '1206')]),
        ),
        migrations.AlterField(
            model_name='storage',
            name='sn',
            field=models.CharField(max_length=50, unique=True, null=True, verbose_name='SN\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='storage',
            name='zone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u673a\u67dc\u533a\u57df', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('101', '101'), ('109', '109')]),
        ),
    ]
