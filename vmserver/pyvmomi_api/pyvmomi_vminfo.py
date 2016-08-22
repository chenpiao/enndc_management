#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

"""
Python program for listing the vms on an ESX / vCenter host
"""
import json
import atexit
import sys
import os
sys.path.append('E:/GitWorkspace/enndc_management')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enndc_management.settings")
import django
django.setup()
from pyVim import connect
from pyVmomi import vmodl
from pyVmomi import vim
from vmserver.models import List
from enndc_management.settings import *

# import tools.cli as cli
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def get_vm_info(virtual_machine):
	"""
	Print information for a particular virtual machine or recurse into a
	folder with depth protection
	"""
	summary = virtual_machine.summary
	guest = virtual_machine.guest
	config = virtual_machine.config
	runtime = virtual_machine.runtime
	try:
		mem = int(config.hardware.memoryMB) / 1024
	except Exception, e:
		print '%s has an mem error' % summary.config.name
		mem = None
	try:
		total_hard_disk = int(summary.storage.committed + summary.storage.uncommitted)
		total_hard_disk = round(total_hard_disk / 1024 / 1024 / 1024, 2) - mem
	except Exception, e:
		print '%s has an disk error' % summary.config.name
		total_hard_disk = None
	print '1'
	vm_data = {
		'uuid': summary.config.instanceUuid,
		'list_name': summary.config.name,
		'hostname': guest.hostName,
		'template': summary.config.template,
		'ip': summary.guest.ipAddress,
		'os': guest.guestFamily,
		'os_version': guest.guestFullName,
		'cpu': config.hardware.numCPU,
		'mem': mem,
		'total_hard_disk': total_hard_disk,
		'tools_status': guest.toolsStatus,
		'guest_status': guest.guestState,
		'power_status': summary.runtime.powerState,
		'vc': runtime.host.summary.managementServerIp,
		'esxi_host': runtime.host.name
	}
	# return vm_data

	# db_uuid_list = []
	# uuids = List.objects.all().values('instance_uuid')
	# for uuid in uuids:
	#     db_uuid_list.append(uuid['instance_uuid'])
	# if vm_data['uuid'] in db_uuid_list:

	obj, created = List.objects.update_or_create(instance_uuid=vm_data['uuid'])

	obj.instance_uuid = vm_data['uuid']
	obj.list_name = vm_data['list_name']
	obj.hostname = vm_data['hostname']
	obj.ip = vm_data['ip']
	obj.os = vm_data['os']
	obj.os_version = vm_data['os_version']
	obj.total_hard_disk = vm_data['total_hard_disk']
	obj.cpu = vm_data['cpu']
	obj.mem = vm_data['mem']
	obj.tools_status = vm_data['tools_status']
	obj.guest_status = vm_data['guest_status']
	obj.vc = vm_data['vc']
	obj.esxi_host = vm_data['esxi_host']
	obj.power_status = vm_data['power_status']
	obj.template = vm_data['template']
	obj.save()
	# 更新


def main():
	"""
	Simple command-line program for listing the virtual machines on a system.
	"""

	# args = cli.get_args()
	vm_data_list = []
	for VC in VC_POOL.keys():
		try:
			service_instance = connect.SmartConnect(host=VC,
													user=USER,
													pwd=PASSWORD)

			atexit.register(connect.Disconnect, service_instance)

			content = service_instance.RetrieveContent()

			container = content.rootFolder  # starting point to look into
			viewType = [vim.VirtualMachine]  # object types to look for
			recursive = True  # whether we should look into it recursively
			containerView = content.viewManager.CreateContainerView(
				container, viewType, recursive)

			children = containerView.view
			num = 1
			for child in children:
				# print child  'vim.VirtualMachine:vm-2053'
				get_vm_info(child)  # 每次传入一个vm实例，上面函数dump到文件也是一个vm的信息
		except vmodl.MethodFault as error:
			print("Caught vmodl fault : " + error.msg)
			return -1

	return 22

# Start program
if __name__ == "__main__":
    main()
