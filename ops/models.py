#!usr/bin/env python
# coding:utf-8
import sys
from django.db import models
from django.contrib.auth.models import User
from settings import *

from asset.models import NetworkDevice
from asset.models import Host
from asset.models import IndustryGroup
# from enn_ansible_api import save_info

reload(sys)
sys.setdefaultencoding('utf8')

# Create your models here.

class VspherePool(models.Model):
    pool_name = models.CharField(u'资源池', max_length=20, unique=True)
    pool_id = models.CharField(u'资源池ID', max_length=20, primary_key=True, unique=True)
    pool_desc = models.CharField(u'描述', max_length=20, null=True)
    born_time = models.DateTimeField(u'创建时间', auto_now_add=True, editable=False, blank=True, null=True)
    update_time = models.DateTimeField(u'上次修改时间', auto_now=True, editable=True, blank=True, null=True)
    # poll_address = models.CharField(u'位置', choices=DataCenterAddress_choices, max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = '资源池'
        verbose_name_plural = '资源池'

    def __unicode__(self):
        return self.pool_name


class HostInfo(models.Model):
    sn = models.ForeignKey(Host, verbose_name='SN号', db_column='sn', to_field='sn')
    hostname = models.CharField(u'物理主机名', max_length=255, blank=True)
    ip = models.GenericIPAddressField(u'物理主机IP地址')
    manage_ip = models.GenericIPAddressField(verbose_name='远控卡IP', null=True, blank=True)
    app_name = models.CharField(u'主机应用名称', max_length=100, blank=True, null=True)
    app_description = models.CharField(u'主机应用描述', max_length=100, blank=True, null=True)
    Cabinet = models.CharField(u'机柜位置', max_length=10, blank=True, null=True)
    OS = models.CharField(u'操作系统', choices=OS_choices, max_length=50, blank=True, null=True)
    OsVersion = models.CharField(u'操作系统版本号', choices=OsVersion_choices, max_length=50, blank=True, null=True)
    Cluster = models.NullBooleanField(u'集群', default=False, blank=True, null=True)
    TotalHardDisk = models.CharField(u'总硬盘容量', max_length=10, blank=True, null=True)
    CPU = models.CharField(u'CPU核心数量', max_length=10, blank=True, null=True)
    CpuMainFrequency = models.CharField(u'CPU主频', max_length=10, blank=True, null=True)
    mem = models.IntegerField(u'内存', null=True, blank=True)
    Raid = models.CharField(u'磁盘阵列信息', choices=Raid_choices, max_length=10, blank=True, null=True)
    fibrechannelhbacards = models.NullBooleanField(u'光纤通道卡', default=False, blank=True, null=True)
    fiberswitchport = models.CharField(u'光纤交换机端口', max_length=30, blank=True, null=True)
    Domain = models.CharField(u'域信息', choices=Domain_choices, max_length=20, blank=True, null=True)
    # app_user = models.ForeignKey(User, verbose_name='应用管理员', related_name='app_user', null=True)
    # PriAdmin = models.ForeignKey(User, verbose_name='管理员', related_name='admin', null=True)
    dmz = models.NullBooleanField(u'DMZ', default=False)
    pool = models.ForeignKey(VspherePool, verbose_name='资源池')
    type = models.CharField(u'应用服务类别', choices=type_choices, max_length=10, blank=True)
    delivery_time = models.DateField(u'资源交付时间', blank=True, null=True)
    datacenter_address = models.CharField(u'位置', max_length=10, null=True, blank=True)
    born_time = models.DateTimeField(u'创建时间', auto_now_add=True, editable=False, blank=True, null=True)
    update_time = models.DateTimeField(u'上次修改时间', auto_now=True, editable=True, blank=True, null=True)
    '''
    def save(self, *args, **kwargs):
        ip = self.ip
        with open('inventory', 'w') as f:
            f.write(json.dumps(ip))
        #save_info(ip)
        # ansible_api.save_info(ip)
        super(HostInfo, self).save(self, *args, **kwargs)  # 调用save
    '''

    class Meta:
        verbose_name = '物理主机'
        verbose_name_plural = '物理主机'

    def __unicode__(self):
        return self.hostname


class NetworkDeviceInfo(models.Model):
    # 网络设备信息
    network_device = models.ForeignKey(NetworkDevice, verbose_name='挂载设备', null=True, blank=True)
    sn = models.CharField('SN号', max_length=50, null=True, blank=True)
    company_name = models.CharField('企业名称', max_length=50, null=True, blank=True)
    dc_location = models.NullBooleanField('是否数据中心', max_length=50, null=True, blank=True)
    industry_group = models.ForeignKey(IndustryGroup, null=True, blank=True)


class VMServer(models.Model):
    hostname = models.CharField(u'主机名', max_length=255, null=True, unique=True)
    ip = models.GenericIPAddressField(u'IP地址')
    app_name = models.CharField(u'应用名称', max_length=30, blank=True, null=True)
    app_role = models.CharField(u'应用角色', max_length=30, blank=True, null=True)
    app_description = models.CharField(u'应用描述', max_length=100, blank=True, null=True)
    type = models.CharField(u'类别', choices=type_choices, max_length=10, blank=True, null=True)
    # app_admin = models.ForeignKey(User, verbose_name='应用管理员', blank=True, null=True, to_field='username')
    admin_con = models.ForeignKey('Contact', verbose_name='管理员', to_field='name')
    # app_admin_contact = models.CharField('联系电话', max_length=100, blank=True, null=True)
    # app_admin_mail = models.CharField('联系邮箱', max_length=100, blank=True, null=True)
    os = models.CharField(u'操作系统', choices=OS_choices, max_length=50, blank=True, null=True)
    os_version = models.CharField(u'操作系统版本号', choices=OsVersion_choices, max_length=50, blank=True, null=True)
    cluster = models.NullBooleanField(u'集群', default=False, blank=True, null=True)
    pool_id = models.ForeignKey(VspherePool, verbose_name='资源池')
    hard_disk = models.CharField(u'硬盘容量', max_length=10, blank=True, null=True)
    total_hard_disk = models.CharField(u'总硬盘容量', max_length=10, blank=True, null=True)
    cpu = models.IntegerField(u'CPU核心数量', blank=True, null=True)
    mem = models.CharField(u'内存', max_length=5, blank=True, null=True)
    domain = models.CharField(u'域信息', choices=Domain_choices, max_length=20, blank=True, null=True)
    create_time = models.DateField(u'资源交付时间', max_length=20, null=True)
    delete_time = models.DateField(u'资源删除时间', max_length=20, blank=True, null=True)
    industry_groupName = models.ForeignKey(IndustryGroup, to_field='name', verbose_name='计费组', null=True)
    born_time = models.DateTimeField(u'创建时间', auto_now_add=True, editable=False, blank=True, null=True)
    update_time = models.DateTimeField(u'上次修改时间', auto_now=True, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = '虚拟主机'
        verbose_name_plural = '虚拟主机'

    def __unicode__(self):
        return self.hostname  # 这段admin首页显示models的表


class Contact(models.Model):
    name = models.CharField('ad账号', max_length=50, unique=True)
    cn_name = models.CharField('姓名', max_length=50, null=True)
    phone = models.CharField('联系电话', max_length=50, null=True)
    mail = models.EmailField('联系邮箱', null=True)

    class Meta:
        verbose_name = '联系人'
        verbose_name_plural = '联系人'

    def __unicode__(self):
        return self.name
