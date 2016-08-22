# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0006_auto_20160504_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='location',
            field=models.CharField(max_length=10, verbose_name=b'\xe5\xad\x98\xe6\x94\xbe\xe4\xbd\x8d\xe7\xbd\xae', choices=[('yz', '\u4ea6\u5e84\u4e9a\u592a\u4e2d\u7acb'), ('yj', '\u71d5\u90ca\u5149\u73af\u65b0\u7f51'), ('lfxx', '\u5eca\u574a\u4fe1\u606f\u5927\u53a6'), ('lfxz', '\u5eca\u574a\u65b0\u667a\u673a\u623f'), ('znds', '\u667a\u80fd\u5927\u53a6\u673a\u623f'), ('xarq', '\u65b0\u5965\u71c3\u6c14\u4f01\u4e1a'), ('other', '\u5176\u4ed6')]),
        ),
        migrations.AlterField(
            model_name='host',
            name='idc',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae\xe4\xb8\xad\xe5\xbf\x83', choices=[('yz', '\u4ea6\u5e84\u4e9a\u592a\u4e2d\u7acb'), ('yj', '\u71d5\u90ca\u5149\u73af\u65b0\u7f51'), ('lfxx', '\u5eca\u574a\u4fe1\u606f\u5927\u53a6'), ('lfxz', '\u5eca\u574a\u65b0\u667a\u673a\u623f'), ('znds', '\u667a\u80fd\u5927\u53a6\u673a\u623f'), ('xarq', '\u65b0\u5965\u71c3\u6c14\u4f01\u4e1a'), ('other', '\u5176\u4ed6')]),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='idc',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae\xe4\xb8\xad\xe5\xbf\x83', choices=[('yz', '\u4ea6\u5e84\u4e9a\u592a\u4e2d\u7acb'), ('yj', '\u71d5\u90ca\u5149\u73af\u65b0\u7f51'), ('lfxx', '\u5eca\u574a\u4fe1\u606f\u5927\u53a6'), ('lfxz', '\u5eca\u574a\u65b0\u667a\u673a\u623f'), ('znds', '\u667a\u80fd\u5927\u53a6\u673a\u623f'), ('xarq', '\u65b0\u5965\u71c3\u6c14\u4f01\u4e1a'), ('other', '\u5176\u4ed6')]),
        ),
        migrations.AlterField(
            model_name='storage',
            name='idc',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u6570\u636e\u4e2d\u5fc3', choices=[('yz', '\u4ea6\u5e84\u4e9a\u592a\u4e2d\u7acb'), ('yj', '\u71d5\u90ca\u5149\u73af\u65b0\u7f51'), ('lfxx', '\u5eca\u574a\u4fe1\u606f\u5927\u53a6'), ('lfxz', '\u5eca\u574a\u65b0\u667a\u673a\u623f'), ('znds', '\u667a\u80fd\u5927\u53a6\u673a\u623f'), ('xarq', '\u65b0\u5965\u71c3\u6c14\u4f01\u4e1a'), ('other', '\u5176\u4ed6')]),
        ),
        migrations.AlterField(
            model_name='tools',
            name='location',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xad\x98\xe6\x94\xbe\xe4\xbd\x8d\xe7\xbd\xae', choices=[('yz', '\u4ea6\u5e84\u4e9a\u592a\u4e2d\u7acb'), ('yj', '\u71d5\u90ca\u5149\u73af\u65b0\u7f51'), ('lfxx', '\u5eca\u574a\u4fe1\u606f\u5927\u53a6'), ('lfxz', '\u5eca\u574a\u65b0\u667a\u673a\u623f'), ('znds', '\u667a\u80fd\u5927\u53a6\u673a\u623f'), ('xarq', '\u65b0\u5965\u71c3\u6c14\u4f01\u4e1a'), ('other', '\u5176\u4ed6')]),
        ),
    ]
