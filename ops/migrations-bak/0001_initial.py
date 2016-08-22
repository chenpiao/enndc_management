# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=255, unique=True, null=True, verbose_name='\u7269\u7406\u4e3b\u673a\u540d')),
                ('ip', models.GenericIPAddressField(verbose_name='\u7269\u7406\u4e3b\u673aIP\u5730\u5740')),
                ('app_name', models.CharField(max_length=100, null=True, verbose_name='\u4e3b\u673a\u5e94\u7528\u540d\u79f0', blank=True)),
                ('app_description', models.CharField(max_length=100, null=True, verbose_name='\u4e3b\u673a\u5e94\u7528\u63cf\u8ff0', blank=True)),
                ('Cabinet', models.CharField(max_length=10, null=True, verbose_name='\u673a\u67dc\u4f4d\u7f6e', blank=True)),
                ('OS', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf', choices=[('Microsoft Windows', 'Microsoft Windows'), ('Linux', 'Linux'), ('VMware ESX Server', 'VMware ESX Server')])),
                ('OsVersion', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c\u53f7', choices=[('CentOS 5_x64', 'CentOS 5 (64\u4f4d)'), ('CentOS 5.8_x64', 'CentOS 5.8 (64\u4f4d)'), ('CentOS 7_x64', 'CentOS 7 (64\u4f4d)'), ('CentOS 6.5_x64', 'CentOS 6.5 (64\u4f4d)'), ('CentOS 6.7_x64', 'CentOS 6.7 (64\u4f4d)'), ('Linux\u5b9a\u5236', 'Linux\u5b9a\u5236'), ('Microsoft Windows 7', 'Microsoft Windows 7'), ('Microsoft Windows Server 2003', 'Microsoft Windows Server 2003'), ('Microsoft Windows Server 2008', 'Microsoft Windows Server 2008'), ('Microsoft Windows Server 2008 R2', 'Microsoft Windows Server 2008 R2'), ('Microsoft Windows XP Professional', 'Microsoft Windows XP Professional'), ('RHEL 6.5_x64', 'RHEL 6.5_x64'), ('RHEL 5.4_x64', 'RHEL 5.4_x64'), ('Ubuntu 12_x64', 'Ubuntu 12_x64'), ('Ubuntu Linux_x64', 'Ubuntu Linux_x64'), ('ESXI 5.0', 'ESXI 5.0'), ('ESXI 5.1 U3', 'ESXI 5.1 U3'), ('Ubuntu Linux_x64', 'Ubuntu Linux_x64')])),
                ('Cluster', models.NullBooleanField(default=False, verbose_name='\u96c6\u7fa4')),
                ('TotalHardDisk', models.CharField(max_length=10, null=True, verbose_name='\u603b\u786c\u76d8\u5bb9\u91cf', blank=True)),
                ('CPU', models.CharField(max_length=10, null=True, verbose_name='CPU\u6838\u5fc3\u6570\u91cf', blank=True)),
                ('CpuMainFrequency', models.CharField(max_length=10, null=True, verbose_name='CPU\u4e3b\u9891', blank=True)),
                ('mem', models.IntegerField(null=True, verbose_name='\u5185\u5b58', blank=True)),
                ('Raid', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u78c1\u76d8\u9635\u5217\u4fe1\u606f', choices=[('1', 'raid1'), ('2', 'raid2'), ('5', 'raid5'), ('0', 'raid0'), ('0+1', 'raid0+1')])),
                ('fibrechannelhbacards', models.NullBooleanField(default=False, verbose_name='\u5149\u7ea4\u901a\u9053\u5361')),
                ('fiberswitchport', models.CharField(max_length=30, null=True, verbose_name='\u5149\u7ea4\u4ea4\u6362\u673a\u7aef\u53e3', blank=True)),
                ('Domain', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u57df\u4fe1\u606f', choices=[('addom.xinaogroup.com', 'addom.xinaogroup.com'), ('adlab.xinaogroup.com', 'adlab.xinaogroup.com'), ('test.xinaogroup.com', 'test.xinaogroup.com')])),
                ('dmz', models.NullBooleanField(default=False, verbose_name='DMZ')),
                ('type', models.CharField(max_length=10, verbose_name='\u5e94\u7528\u670d\u52a1\u7c7b\u522b', choices=[('pro', '\u751f\u4ea7'), ('dev_test', '\u5f00\u53d1\u6d4b\u8bd5'), ('lib', '\u5b9e\u9a8c')])),
                ('delivery_time', models.DateField(verbose_name='\u8d44\u6e90\u4ea4\u4ed8\u65f6\u95f4')),
                ('datacenter_address', models.CharField(max_length=10, null=True, verbose_name='\u4f4d\u7f6e', blank=True)),
                ('born_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4e0a\u6b21\u4fee\u6539\u65f6\u95f4', null=True)),
            ],
            options={
                'verbose_name': '\u7269\u7406\u4e3b\u673a',
                'verbose_name_plural': '\u7269\u7406\u4e3b\u673a',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=255, unique=True, null=True, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.GenericIPAddressField(verbose_name='IP\u5730\u5740')),
                ('app_name', models.CharField(max_length=30, null=True, verbose_name='\u5e94\u7528\u540d\u79f0', blank=True)),
                ('appRole', models.CharField(max_length=30, null=True, verbose_name='\u5e94\u7528\u89d2\u8272', blank=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u7c7b\u522b', choices=[('pro', '\u751f\u4ea7'), ('dev_test', '\u5f00\u53d1\u6d4b\u8bd5'), ('lib', '\u5b9e\u9a8c')])),
                ('app_description', models.CharField(max_length=100, null=True, verbose_name='\u5e94\u7528\u63cf\u8ff0', blank=True)),
                ('OS', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf', choices=[('Microsoft Windows', 'Microsoft Windows'), ('Linux', 'Linux'), ('VMware ESX Server', 'VMware ESX Server')])),
                ('OsVersion', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c\u53f7', choices=[('CentOS 5_x64', 'CentOS 5 (64\u4f4d)'), ('CentOS 5.8_x64', 'CentOS 5.8 (64\u4f4d)'), ('CentOS 7_x64', 'CentOS 7 (64\u4f4d)'), ('CentOS 6.5_x64', 'CentOS 6.5 (64\u4f4d)'), ('CentOS 6.7_x64', 'CentOS 6.7 (64\u4f4d)'), ('Linux\u5b9a\u5236', 'Linux\u5b9a\u5236'), ('Microsoft Windows 7', 'Microsoft Windows 7'), ('Microsoft Windows Server 2003', 'Microsoft Windows Server 2003'), ('Microsoft Windows Server 2008', 'Microsoft Windows Server 2008'), ('Microsoft Windows Server 2008 R2', 'Microsoft Windows Server 2008 R2'), ('Microsoft Windows XP Professional', 'Microsoft Windows XP Professional'), ('RHEL 6.5_x64', 'RHEL 6.5_x64'), ('RHEL 5.4_x64', 'RHEL 5.4_x64'), ('Ubuntu 12_x64', 'Ubuntu 12_x64'), ('Ubuntu Linux_x64', 'Ubuntu Linux_x64'), ('ESXI 5.0', 'ESXI 5.0'), ('ESXI 5.1 U3', 'ESXI 5.1 U3'), ('Ubuntu Linux_x64', 'Ubuntu Linux_x64')])),
                ('Cluster', models.NullBooleanField(default=False, verbose_name='\u96c6\u7fa4')),
                ('HardDisk', models.CharField(max_length=10, null=True, verbose_name='\u786c\u76d8\u5bb9\u91cf', blank=True)),
                ('TotalHardDisk', models.CharField(max_length=10, null=True, verbose_name='\u603b\u786c\u76d8\u5bb9\u91cf', blank=True)),
                ('CPU', models.IntegerField(null=True, verbose_name='CPU\u6838\u5fc3\u6570\u91cf', blank=True)),
                ('Mem', models.CharField(max_length=5, null=True, verbose_name='\u5185\u5b58', blank=True)),
                ('Domain', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u57df\u4fe1\u606f', choices=[('addom.xinaogroup.com', 'addom.xinaogroup.com'), ('adlab.xinaogroup.com', 'adlab.xinaogroup.com'), ('test.xinaogroup.com', 'test.xinaogroup.com')])),
                ('create_time', models.DateField(max_length=20, null=True, verbose_name='\u8d44\u6e90\u4ea4\u4ed8\u65f6\u95f4')),
                ('delete_time', models.DateField(max_length=20, null=True, verbose_name='\u8d44\u6e90\u5220\u9664\u65f6\u95f4', blank=True)),
                ('IndustryGroupName', models.CharField(max_length=30, null=True, verbose_name=b'\xe8\xae\xa1\xe8\xb4\xb9\xe7\xbb\x84', choices=[('\u65b0\u667a\u4e91', '\u65b0\u667a\u4e91'), ('E\u57ceE\u5bb6', 'E\u57ceE\u5bb6'), ('E\u57ce\u5230\u5bb6', 'E\u57ce\u5230\u5bb6'), ('\u5317\u90e8\u6e7e\u65c5\u6e38', '\u5317\u90e8\u6e7e\u65c5\u6e38'), ('\u8d22\u52a1\u516c\u53f8', '\u8d22\u52a1\u516c\u53f8'), ('\u96c6\u56e2\u603b\u90e8', '\u96c6\u56e2\u603b\u90e8'), ('\u80fd\u6e90\u5206\u9500', '\u80fd\u6e90\u5206\u9500'), ('\u80fd\u6e90\u7814\u7a76\u9662', '\u80fd\u6e90\u7814\u7a76\u9662'), ('\u592a\u9633\u80fd\u6e90', '\u592a\u9633\u80fd\u6e90'), ('\u5a01\u8fdc\u751f\u5316', '\u5a01\u8fdc\u751f\u5316'), ('\u65b0\u535a\u5353\u521b', '\u65b0\u535a\u5353\u521b'), ('\u65b0\u535a\u5353\u7545', '\u65b0\u535a\u5353\u7545'), ('\u65b0\u5730\u5de5\u7a0b', '\u65b0\u5730\u5de5\u7a0b'), ('\u65b0\u7ece\u5730\u4ea7', '\u65b0\u7ece\u5730\u4ea7'), ('\u65b0\u7ece\u5065\u5eb7', '\u65b0\u7ece\u5065\u5eb7'), ('\u65b0\u82d1\u9633\u5149', '\u65b0\u82d1\u9633\u5149'), ('\u65b0\u667a\u4e92\u8054\u7f51', '\u65b0\u667a\u4e92\u8054\u7f51'), ('\u667a\u80fd\u80fd\u6e90', '\u667a\u80fd\u80fd\u6e90')])),
                ('born_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4e0a\u6b21\u4fee\u6539\u65f6\u95f4', null=True)),
            ],
            options={
                'verbose_name': '\u865a\u62df\u4e3b\u673a',
                'verbose_name_plural': '\u865a\u62df\u4e3b\u673a',
            },
        ),
        migrations.CreateModel(
            name='VspherePool',
            fields=[
                ('pool_name', models.CharField(unique=True, max_length=20, verbose_name='\u8d44\u6e90\u6c60')),
                ('pool_id', models.CharField(max_length=20, unique=True, serialize=False, verbose_name='\u8d44\u6e90\u6c60ID', primary_key=True)),
                ('pool_desc', models.CharField(max_length=20, null=True, verbose_name='\u63cf\u8ff0')),
                ('born_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4e0a\u6b21\u4fee\u6539\u65f6\u95f4', null=True)),
            ],
            options={
                'verbose_name': '\u8d44\u6e90\u6c60',
                'verbose_name_plural': '\u8d44\u6e90\u6c60',
            },
        ),
        migrations.AddField(
            model_name='server',
            name='pool_id',
            field=models.ForeignKey(verbose_name=b'\xe8\xb5\x84\xe6\xba\x90\xe6\xb1\xa0', to='ops.VspherePool'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='pool',
            field=models.ForeignKey(verbose_name=b'\xe8\xb5\x84\xe6\xba\x90\xe6\xb1\xa0', to='ops.VspherePool'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='sn',
            field=models.ForeignKey(verbose_name=b'SN\xe5\x8f\xb7', to='asset.Host'),
        ),
    ]
