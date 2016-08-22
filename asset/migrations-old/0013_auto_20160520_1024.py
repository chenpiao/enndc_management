# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0012_auto_20160512_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostsparepart',
            name='host',
            field=models.ForeignKey(verbose_name=b'\xe6\x8c\x82\xe8\xbd\xbd\xe4\xb8\xbb\xe6\x9c\xba', to_field=b'sn', blank=True, to='asset.Host', null=True),
        ),
        migrations.AlterField(
            model_name='networksparepart',
            name='host',
            field=models.ForeignKey(verbose_name=b'\xe6\x8c\x82\xe8\xbd\xbd\xe8\xae\xbe\xe5\xa4\x87', to_field=b'sn', blank=True, to='asset.NetworkDevice', null=True),
        ),
        migrations.AlterField(
            model_name='storagesparepart',
            name='host',
            field=models.ForeignKey(verbose_name=b'\xe5\xad\x98\xe5\x82\xa8\xe5\xa4\x87\xe4\xbb\xb6', to_field=b'sn', blank=True, to='asset.Storage', null=True),
        ),
    ]
