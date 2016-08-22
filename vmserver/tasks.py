#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

import datetime
import json
from djcelery import models as celery_models
from django.utils import timezone
from celery import task
from vmserver.models import List, ListInfoLog
from django.core.mail import EmailMultiAlternatives, send_mail
import xlwt
from enndc_management.settings import *
from pyvmomi_api.batch_get import gather_vm_info, execute_compare
from pyVmomi import vmodl
from pyVmomi import vim
from pyVim import connect
from vmserver.tools import vc_all_uuid
from vmserver.tools import VCenterInfo
import atexit
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import logging
LOG = logging.getLogger('vmserver')
BUG = logging.getLogger('request')


@task()
def add(x, y):
    return x + y


def create_task(name, task, task_args, crontab_time):
    '''
    创建任务
    name       # 任务名字
    task       # 执行的任务 "myapp.tasks.add"
    task_args  # 任务参数  {"x":1, "Y":1}
    crontab_time # 定时任务时间 格式：
        {
          'month_of_year': 9  # 月份
          'day_of_month': 5   # 日期
          'hour': 01         # 小时
          'minute':05  # 分钟
        }

    '''
    # task任务， created是否定时创建
    task, created = celery_models.PeriodicTask.objects.get_or_create(
        name=name,
        task=task)
    # 获取 crontab
    crontab = celery_models.CrontabSchedule.objects.filter(
        **crontab_time).first()
    if crontab is None:
        # 如果没有就创建，有的话就继续复用之前的crontab
        crontab = celery_models.CrontabSchedule.objects.create(
            **crontab_time)
    task.crontab = crontab  # 设置crontab
    task.enabled = True  # 开启task
    task.kwargs = json.dumps(task_args)  # 传入task参数
    expiration = timezone.now() + datetime.timedelta(day=1)
    task.expires = expiration  # 设置任务过期时间为现在时间的一天以后
    task.save()
    return True


def disable_task(name):
    '''
    关闭任务
    '''
    try:
        task = celery_models.PeriodicTask.objects.get(name=name)
        task.enabled = False  # 设置关闭
        task.save()
        return True
    except celery_models.PeriodicTask.DoesNotExist:
        return True


def grave_warning_report():
    # This method has already been abandoned
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2
    font0.bold = True

    style0 = xlwt.XFStyle()
    style0.font = font0

    wb = xlwt.Workbook()
    ws = wb.add_sheet(u'信息完整性报表-严重级别', cell_overwrite_ok=True)
    head = [u'清单名', u'主机名', u'IP地址', u'操作系统', u'VC地址']
    cloumn = 0
    for header in head:
        ws.write(0, cloumn, header, style0)
        cloumn += 1

    all_info = List.objects.all()
    row = 1
    for obj in all_info:
        if obj.app_name is None and obj.app_admin is None and obj.template == 'False':
            list_name = obj.list_name
            hostname = obj.hostname
            ip = obj.ip
            os = obj.os
            vc = obj.vc
            ws.write(row, 0, list_name)
            ws.write(row, 1, hostname)
            ws.write(row, 2, ip)
            ws.write(row, 3, os)
            ws.write(row, 4, vc)
            row += 1
    timestamp = str(datetime.datetime.now()).split('.')[0].replace(' ', '_').replace(':', '-')
    filename = 'grave_warning_report' + timestamp
    wb.save('/tmp/cmdb_report/{0}.xls'.format(filename))

    subject = u'生产系统VM信息完整性报告-严重级别'
    content = u'附件中服务器应用信息、管理员信息、归属信息均不完整，请访问CMDB系统尽快完善'
    mail_from = 'eCloud@enn.cn'
    mail_to = ['zhangyang@enn.cn', 'qiaojian@enn.cn', 'sunyawei@enn.cn', 'sunyaxiong@enn.cn']
    msg = EmailMultiAlternatives(subject, content, mail_from, mail_to)
    msg.attach_file('/tmp/cmdb_report/{0}.xls'.format(filename))
    msg.send()

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
        'esxi_host': runtime.host.name,
    }

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

def batch_get():
    """
    # This method has already been abandoned
    method to get vminfo from VC
    """

    for VC in VC_POOL.keys():
        try:
            service_instance = connect.SmartConnect(host=VC,
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
            num = 0
            for child in children:
                # print child
                data = gather_vm_info(child)
                #print 'ok'
                execute_compare(data)
                #print 'compare ok'
                num += 1
            print num
            print datetime.datetime.now()
        except vmodl.MethodFault as error:
            print("Caught vmodl fault : " + error.msg)
            return -1

    return 0


'''	
def offline_check():
    for HOST in HOST_POOL:
        try:
            service_instance = connect.SmartConnect(host=HOST,
                                                    user=USER,
                                                    pwd=PASSWORD,)

            atexit.register(connect.Disconnect, service_instance)

            objs = List.objects.filter(vc=HOST).values('instance_uuid','list_name','ip')
            for obj in objs:
                uuid = obj['instance_uuid']

                search_index = service_instance.content.searchIndex
                vm = search_index.FindByUuid(None, uuid, True, True)
                if vm is None:
                    print '{0},is not found, vc:{1}, ln:{2}--{3}'.format(uuid, HOST, obj['list_name'], obj['ip'])

        except vmodl.MethodFault as error:
            print("Caught vmodl fault : " + error.msg)
            return -1

    return 0
'''



def offline_check():
    # This method has already been abandoned
    uuid_list = vc_all_uuid()
    print len(uuid_list)
    objs = List.objects.filter().values('instance_uuid', 'list_name', 'ip')
    all_vm_ins = []
    for obj in objs:
        uuid = obj['instance_uuid']
        vm_ins = {}
        if uuid not in uuid_list:
            vm_ins['uuid'] = uuid
            vm_ins['list_name'] = obj['list_name']
            vm_ins['ip'] = obj['ip']
            all_vm_ins.append(vm_ins)
    subject = u'offline-check:以下cmdb内虚拟机在VC环境中无法找到，请确认是否下线并完善信息。'
    content = json.dumps(all_vm_ins, indent=4)
    mail_from = 'eCloud@enn'
    mail_to = ['zhangyang@enn.cn', 'qiaojian@enn.cn', 'sunyawei@enn.cn', 'sunyaxiong@enn.cn']
    msg = EmailMultiAlternatives(subject, content, mail_from, mail_to)
    msg.send()

@task()
def vm_info_dump():
    # Periodic tasks - get all the vms in VCenter and dump to json file
    for vc in VC_POOL.keys():
        conn = VCenterInfo(vc)
        vm_info_list = conn.get_vc_vm(vc)
        # timestamp = str(datetime.datetime.now()).split('.')[0].replace(' ', '_').replace(':', '-')
        file_name = vc
        json.dump(vm_info_list, open(BASE_DIR + '/vmserver/data/{0}.json'.format(file_name), 'w'), ensure_ascii=False, indent=4)

@task()
def db_info_update():
    # Periodic tasks - json.load() all vms no_charge info and dict update DB
    num = 0
    for vc in VC_POOL.keys():
        info = json.load(open(BASE_DIR + '/vmserver/data/{0}.json'.format(vc), 'r'))
        for vm in info:
            obj = List.objects.filter(instance_uuid=vm['instance_uuid'])
            # print type(obj)
            if len(obj) == 1:
                no_list = ['cpu', 'mem', 'total_hard_disk']
                for key in no_list:
                    vm.pop(key)
                # vm['update_time'] = datetime.datetime.now()
                obj.update(**vm)
            else:
                List.objects.create(**vm)
                num += 1
    print num
@task()
def charge_info_update():
    # cpu mem disk etc  charge info update
    num = 0
    for vc in VC_POOL.keys():
        info = json.load(open(BASE_DIR + '/vmserver/data/{0}.json'.format(vc), 'r'))
        for vm in info:
            try:
                obj = List.objects.get(instance_uuid=vm['instance_uuid'])
                if vm['cpu'] != obj.cpu:
                    LOG.info('{0} has cpu change'.format(obj.list_name))
                    ListInfoLog.objects.create(
                        list_name=vm['list_name'],
                        ip=vm['ip'],
                        vm_ins=obj,
                        col='cpu',
                        val_from=obj.cpu,
                        val_to=vm['cpu'],
                        action_time=datetime.datetime.now()
                    )
                    obj.cpu = vm['cpu']
                    obj.save()
                if vm['mem'] != obj.mem:
                    LOG.info('{0} has mem change'.format(obj.list_name))
                    ListInfoLog.objects.create(
                        list_name=vm['list_name'],
                        ip=vm['ip'],
                        vm_ins=obj,
                        col='mem',
                        val_from=obj.mem,
                        val_to=vm['mem'],
                        action_time=datetime.datetime.now()
                    )
                    obj.mem = vm['mem']
                    obj.save()
                if vm['total_hard_disk'] != obj.total_hard_disk:
                    LOG.info('{0} has disk change'.format(obj.list_name))
                    ListInfoLog.objects.create(
                        list_name=vm['list_name'],
                        ip=vm['ip'],
                        vm_ins=obj,
                        col='total_hard_disk',
                        val_from=obj.total_hard_disk,
                        val_to=vm['total_hard_disk'],
                        action_time=datetime.datetime.now()
                    )
                    obj.total_hard_disk = vm['total_hard_disk']
                    obj.save()
            except Exception, e:
                LOG.info(e.message)
                print vm['instance_uuid']
                List.objects.create(**vm)
                LOG.info('{0}-{1} has created'.format(vm['instance_uuid'], vm['list_name']))
                num += 1
    LOG.info('created {0} vms'.format(num))
@task()	
def off_line_vm():
    # compare the vm of database with VCenter, mark the delete_time
    count = 0
    for vc in VC_POOL.keys():
        objs = List.objects.filter(delete_time=None, vc=vc, template='false')
        conn = VCenterInfo(vc)
        for obj in objs:
            vm = conn.search_vc(obj.instance_uuid)
            if vm is None:
                obj.delete_time = datetime.datetime.now()
                obj.save()
                count += 1
    print count

if __name__ == '__main__':
    grave_warning_report()
