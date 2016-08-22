#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

"""
Python program for listing the vms on an ESX / vCenter host
"""

import sys
import os
sys.path.append('E:/GitWorkspace/enndc_management')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enndc_management.settings")
import django
django.setup()

import atexit
from vmserver.models import List, ListInfoLog
from pyVim import connect
from pyVmomi import vmodl
from pyVmomi import vim
from enndc_management.settings import *
from vmserver import tools
import re
import datetime
import logging
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

logger = logging.getLogger(__name__)


def gather_vm_info(virtual_machine):
    """
    Print information for a particular virtual machine or recurse into a
    folder with depth protection
    """

    data = {}
    summary = virtual_machine.summary
    config = virtual_machine.config
    guest = virtual_machine.guest
    runtime = virtual_machine.runtime
    if hasattr(summary, 'config'):
        if hasattr(config, 'hardware'):
            data['cpu'] = config.hardware.numCPU
            data['mem'] = config.hardware.memoryMB / 1024
            data['total_hard_disk'] = tools.disk_gb(virtual_machine)
            # data['total_hard_disk'] = int(data['total_hard_disk'] / 1024 / 1024 / 1024) - data['mem']
            data['instance_uuid'] = summary.config.instanceUuid
            data['list_name'] = summary.config.name
            data['hostname'] = guest.hostName
            data['template'] = summary.config.template
            data['ip'] = summary.guest.ipAddress
            data['os'] = guest.guestFamily
            data['os_version'] = guest.guestFullName
            data['tools_status'] = guest.toolsStatus
            data['guest_status'] = guest.guestState
            data['power_status'] = summary.runtime.powerState
            data['vc'] = runtime.host.summary.managementServerIp
            data['esxi_host'] = runtime.host.name
    print data['instance_uuid']
    return data


def execute_compare(data):
    # 用来定时获取最新的cpu、mem、disk信息
    try:
        obj = List.objects.get(instance_uuid=data['instance_uuid'])
        if data['cpu'] != obj.cpu:
            # obj.save()
            print 'c'
            ListInfoLog.objects.create(
                list_name=data['list_name'],
                ip=data['ip'],
                vm_ins=obj,
                col='cpu',
                val_from=obj.cpu,
                val_to=data['cpu'],
                action_time=datetime.datetime.now()
            )
            obj.cpu = data['cpu']
            obj.save()
        if data['mem'] != int(obj.mem):
            # obj.save()
            print 'm'
            ListInfoLog.objects.create(
                list_name=data['list_name'],
                ip=data['ip'],
                vm_ins=obj,
                col='mem',
                val_from=obj.mem,
                val_to=data['mem'],
                action_time=datetime.datetime.now()
            )
            obj.mem = data['mem']
            obj.save()
        if data['total_hard_disk'] != long(obj.total_hard_disk):
            print obj
            print type(data['total_hard_disk'])
            print type(obj.total_hard_disk)
            ListInfoLog.objects.create(
                list_name=data['list_name'],
                ip=data['ip'],
                vm_ins=obj,
                col='disk',
                val_from=obj.total_hard_disk,
                val_to=data['total_hard_disk'],
                action_time=datetime.datetime.now()
            )
            obj.total_hard_disk = data['total_hard_disk']
            obj.save()
    except Exception, e:
        print 'uuid not found--- {0}'.format(data['instance_uuid'])
        new_obj = List.objects.get_or_create(
            instance_uuid=data['instance_uuid'],
            list_name=data['list_name'],
            hostname=data['hostname'],
            template=data['template'],
            ip=data['ip'],
            os=data['os'],
            os_version=data['os_version'],
            cpu=data['cpu'],
            mem=data['mem'],
            total_hard_disk=data['total_hard_disk'],
            tools_status=data['tools_status'],
            guest_status=data['guest_status'],
            power_status=data['power_status'],
            vc=data['vc'],
            esxi_host=data['esxi_host'],
        )
        print '{0} is created'.format(new_obj)


def batch_get():
    """
    Simple command-line program for listing the virtual machines on a system.
    """

    for VC in VC_POOL.keys():
        try:
            service_instance = connect.SmartConnect(host=HOST,
                                                    user=USER,
                                                    pwd=PASSWORD,)

            atexit.register(connect.Disconnect, service_instance)

            content = service_instance.RetrieveContent()

            container = content.rootFolder  # starting point to look into
            viewType = [vim.VirtualMachine]  # object types to look for
            recursive = True  # whether we should look into it recursively
            containerView = content.viewManager.CreateContainerView(
                container, viewType, recursive)

            children = containerView.view
            for child in children:
                # print child
                data = gather_vm_info(child)
                execute_compare(data)
            print datetime.datetime.now()
        except vmodl.MethodFault as error:
            print("Caught vmodl fault : " + error.msg)
            return -1

    return 0

# Start program
if __name__ == "__main__":
    pass