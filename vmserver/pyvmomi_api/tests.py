#!usr/bin/env python
# coding:utf-8

from __future__ import division
import sys
import os
sys.path.append('E:/GitWorkspace/enndc_management')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enndc_management.settings")
import django
django.setup()
from pysphere import VIServer, MORTypes, VIProperty
from pysphere.resources import VimService_services as VI
import pysphere
import re
import time
import pprint
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from vmserver.models import *
'''
HOST = "10.32.18.151"
USER = "cmdb"
PASSWORD = "1qazxsw@"

server = VIServer()
server.connect(HOST, USER, PASSWORD)
# print '\033[32mVC connect successful...\033[0m'

vms_info = {}

# VMware API接口定义
properties = [
    'summary.vm',
    'summary.quickStats.uptimeSeconds',
    'summary.runtime.powerState',
    'summary.runtime.host',
    'summary.runtime.powerState',
    'summary.config.instanceUuid',
    'summary.storage.committed',
    'summary.storage.uncommitted',
    'summary.storage.unshared',
    'guest.toolsStatus',
    'guest.guestId',
    'guest.guestFullName',
    'guest.guestFamily',
    'guest.guestState',
    'guest.ipAddress',
    'guest.hostName',
    'name',
    'parent',
    'config.hardware.numCPU',
    'config.hardware.memoryMB'  #32
    # 'resourcePool.summary.name'
]

# 通过_retrieve_properties_traversal方法传入API接口定义拿到对象类型为 VirtualMachine 的信息
props = server._retrieve_properties_traversal(property_names=properties, obj_type='VirtualMachine')
# pprint.pprint(props)
# 通过server.get_hosts()拿到VC下面所有的host信息（字典）；
# 通过这个方法可以把'guest.hostName'取出的MOR对象转换成实际的hostname
# hostname = server.get_hosts().items()

for prop in props:
    mor = prop.Obj
    # pprint.pprint(mor)
    # pprint.pprint(prop.PropSet)
    vm = {}
    for p in prop.PropSet:   # p是每条信息的对象
        vm[p.Name] = p.Val
    vms_info[mor] = vm
    # pprint.pprint(vms_info)  # key=p.obj, value是kv集合

vms_dict = vms_info.values()
# pprint.pprint(vms_dict[0])

for i in range(len(vms_dict)):
    vm = vms_dict[i]
    try:
        uuid = vm['summary.config.instanceUuid']
    except Exception, e:
        print '%(name)s has an uuid error' % vm
        uuid = None
    try:
        list_name = vm['name']
    except Exception, e:
        print '%(name)s has an ip error' % vm
        list_name = None
    try:
        hostname = vm['guest.hostName']
    except Exception, e:
        print '%(name)s has an hostname error' % vm
        hostname = None
    try:
        ip = vm['guest.ipAddress']
    except Exception, e:
        print '%(name)s has an ip error' % vm
        ip = None
    try:
        os = vm['guest.guestFamily']
    except Exception, e:
        print '%(name)s has an os error' % vm
        os = None
    try:
        os_version = vm['guest.guestFullName']
    except Exception, e:
        print '%(name)s has an os_version error' % vm
        os_version = None
    try:
        total_hard_disk = int(vm['summary.storage.committed']+vm['summary.storage.uncommitted'])
        total_hard_disk = round(total_hard_disk / 1024 / 1024 / 1024, 2)
    except Exception, e:
        print '%(name)s has an disk error' % vm
        total_hard_disk = None

    # models save
    vm_ins = List(
        instance_uuid=uuid,
        list_name=list_name,
        hostname=hostname,
        ip=ip,
        os=os,
        os_version=os_version,
        cpu=vm['config.hardware.numCPU'],
        mem=vm['config.hardware.memoryMB'],
        total_hard_disk=total_hard_disk,
        tools_status=vm['guest.toolsStatus'],
        guest_status=vm['guest.guestState'],
        vc=HOST
        # pool_id=pool_id,
    )
    vm_ins.save()
print 'Done !'
    # pprint.pprint(vm['guest.ipAddress'])

# print '\033[32mVC disconnect successful...\033[0m'

server.disconnect()
'''