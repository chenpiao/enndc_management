#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'


import sys
import os
sys.path.append('E:/GitWorkspace/enndc_management')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enndc_management.settings")
import django
django.setup()
import xlwt
import json
from vmserver.models import List
from ops.models import Contact

font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.colour_index = 2
font0.bold = True

style0 = xlwt.XFStyle()
style0.font = font0

wb = xlwt.Workbook()
ws = wb.add_sheet('hostlist')
head = [u'主机名称', u'显示名', u'IP地址', u'应用名称', u'管理员', u'分组名称', u'模板名称', u'主机位置',]
cloumn = 0
for header in head:
    ws.write(0, cloumn, header, style0)
    cloumn += 1

info = json.load(open('../data/10.37.17.190_2016-07-06_15-55-26.json', 'r'), encoding='UTF-8')
row = 1
for vm in info:
    uuid = vm['uuid']
    list_name = vm['list_name']
    hostname = vm['hostname']
    ip = vm['ip']
    group = vm['os']
    if group == 'linuxGuest':
        template = 'Template OS Linux'
    elif group == 'windowsGuest':
        template = 'Template OS Windows'
    else:
        template = ''
    location = u'虚拟机'
    try:
        vm_obj = List.objects.get(instance_uuid=uuid)
        app_name = vm_obj.app_name
        admin = vm_obj.app_admin_id
    except Exception, e:
        print e
        continue
    ws.write(row, 0, hostname)
    ws.write(row, 1, list_name)
    ws.write(row, 2, ip)
    ws.write(row, 3, app_name)
    ws.write(row, 4, admin)
    ws.write(row, 5, group)
    ws.write(row, 6, template)
    ws.write(row, 7, location)
    row += 1
wb.save('10.37.17.190_zab_list_from_json.xls')
