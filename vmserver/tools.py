#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

from pyVmomi import vim
from pyVmomi import vmodl
from pyVim import connect
from enndc_management.settings import *
import paramiko
import atexit
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class ParamikoAPI(object):

    __slots__ = ['host', 'username', 'password', 'ssh', 'hostname']

    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.hostname, username=self.username, password=self.password)

    def excute_shell(self, commands):
        #for command in commands:
        stdin, stdout, stderr = self.ssh.exec_command(commands)
        if stdout:
            return stdout.read()


def comparative(obj, data):

    '''
    该方法用来比较vc取出data与数据库对象个字段比较，待后续完善。
    '''
    data = {}
    cols = data.keys()
    for i in cols:
        if obj.i != data[i]:
            pass
    return None

def disk_gb(virtual_machine):

    '''
    this method used to get disk size(Gb) of a vm
    '''

    config =virtual_machine.config
    devices = config.hardware.device
    disk_kb = 0
    for device in devices:
        if isinstance(device, vim.vm.device.VirtualDisk):
            disk_kb_one = device.capacityInKB
            disk_kb += disk_kb_one
    disk_gb = disk_kb / 1024 / 1024
    return disk_gb


def vc_all_uuid():
    all_list = []
    for HOST in HOST_POOL:
        try:
            service_instance = connect.SmartConnect(host=HOST,
                                                    user=USER,
                                                    pwd=PASSWORD)

            atexit.register(connect.Disconnect, service_instance)

            content = service_instance.RetrieveContent()

            container = content.rootFolder  # starting point to look into
            viewType = [vim.VirtualMachine]  # object types to look for
            recursive = True  # whether we should look into it recursively
            containerView = content.viewManager.CreateContainerView(
                container, viewType, recursive)

            children = containerView.view   # HOST下对象的集合
            for child in children:
                uuid = child.summary.config.instanceUuid
                all_list.append(uuid)
        except vmodl.MethodFault as error:
            print("Caught vmodl fault : " + error.msg)
            return -1

    return all_list

def get_public_ip(vm):
    guest = vm.guest
    summary = vm.summary
    if guest is not None:
        try:
            ip_list = [ip.ipAddress for nic in guest.net for ip in nic.ipConfig.ipAddress if ip.state == 'preferred']
            public_ip = [ip for ip in ip_list if ip.startswith('10')][0]
            return public_ip
        except Exception, e:
            # print e.message
            public_ip = summary.guest.ipAddress
            return public_ip
    else:
        return None

class VCenterInfo(object):

    def __init__(self, ip, user=USER, passwd=PASSWORD):
        # init connection
        self.ip = ip
        self.user = user
        self.password = passwd
        self.si = connect.SmartConnect(
            host=self.ip,
            user=self.user,
            pwd=self.password
        )

    def vms_info(self):
        # vm obj list
        atexit.register(connect.Disconnect, self.si)
        content = self.si.RetrieveContent()
        container = content.rootFolder
        VmViewType = [vim.VirtualMachine]
        recursive = True
        VmContainerView = content.viewManager.CreateContainerView(
            container, VmViewType, recursive)
        vm_children = VmContainerView.view

        return vm_children

    def hosts_info(self):
        # host obj list
        atexit.register(connect.Disconnect, self.si)
        content = self.si.RetrieveContent()
        container = content.rootFolder
        HostViewType = [vim.HostSystem]
        recursive = True
        HostContainerView = content.viewManager.CreateContainerView(
            container, HostViewType, recursive)
        host_children = HostContainerView.view

        return host_children

    def resource_pool_info(self):
        atexit.register(connect.Disconnect, self.si)
        content = self.si.RetrieveContent()
        container = content.rootFolder
        resourcePoolViewType = [vim.ResourcePool]
        recursive = True
        resourcePoolContainerView = content.viewManager.CreateContainerView(
            container, resourcePoolViewType, recursive)
        pool_children = resourcePoolContainerView.view
        return pool_children

    def host_mem(self):
        hosts = self.hosts_info()
        vc_usage_mem = 0
        vc_all_mem = 0
        for host in hosts:
            host_mem_usage = host.summary.quickStats.overallMemoryUsage
            host_all_mem = host.hardware.memorySize / 1024 / 1024
            vc_usage_mem += host_mem_usage
            vc_all_mem += host_all_mem
        vc_mem_percentage = format(float(vc_usage_mem) / float(vc_all_mem), '.4')
        return vc_mem_percentage

    def usage(self):

        pools = self.resource_pool_info()
        print type(pools)
        for pool in pools:
            print 'name:', pool.summary.name
            print pool.runtime.memory

    def get_vc_vm(self, vc):
        vms = self.vms_info()
        data_list = []
        for vm in vms:
            data = {}
            summary = vm.summary
            guest = vm.guest
            config = vm.config
            runtime = vm.runtime
            devices = vm.config.hardware.device
            # if hasattr(summary, 'config')
            disk_kb = 0
            for device in devices:
                if isinstance(device, vim.vm.device.VirtualDisk):
                    disk_kb_one = device.capacityInKB
                    disk_kb += disk_kb_one
            total_disk_gb = disk_kb / 1024 / 1024
            data['instance_uuid'] = config.instanceUuid
            data['list_name'] = config.name
            data['hostname'] = guest.hostName
            data['ip'] = get_public_ip(vm)
            data['os'] = guest.guestFamily
            data['os_version'] = guest.guestFullName
            if hasattr(config, 'hardware'):
                data['cpu'] = config.hardware.numCPU
                data['mem'] = config.hardware.memoryMB / 1024
            data['total_hard_disk'] = total_disk_gb
            data['tools_status'] = guest.toolsStatus
            data['guest_status'] = guest.guestState
            data['power_status'] = runtime.powerState
            data['vc'] = vc
            data['esxi_host'] = runtime.host.name
            data['template'] = summary.config.template
            data_list.append(data)

        return data_list

    def get_host_info(self):
        hosts = self.hosts_info()
        hosts_list = []
        for host in hosts:
            data = {}
            summary = host.summary
            data['name'] = host.name
            if hasattr(summary, 'quickStats'):
                data['cpu_usage'] = summary.quickStats.overallCpuUsage
                data['mem_usage'] = summary.quickStats.overallMemoryUsage
            if hasattr(summary, 'hardware'):
                data['host_uuid'] = summary.hardware.uuid
                data['host_model'] = summary.hardware.model
                data['host_vendor'] = summary.hardware.vendor
                data['mem'] = summary.hardware.memorySize / 1024 / 1024 # long type
                data['cpu_model'] = summary.hardware.cpuModel
                data['cpu_mhz'] = summary.hardware.cpuMhz
                data['cpu_pkg'] = summary.hardware.numCpuPkgs
                data['cpu_cores'] = summary.hardware.numCpuCores
                data['cpu_threads'] = summary.hardware.numCpuThreads
                data['num_nics'] = summary.hardware.numNics
                data['num_hbas'] = summary.hardware.numHBAs
                hosts_list.append(data)
        return hosts_list

    def search_vc(self, instance_uuid):
        # search func, be prepare to use
        search_index = self.si.content.searchIndex
        vm = search_index.FindByUuid(None, instance_uuid, True, True)
        return vm


# Start program
if __name__ == "__main__":
    conn = ParamikoAPI('10.37.149.85', 'appadmin', 'Xinao.com123123')
    conn.excute_shell('date')
