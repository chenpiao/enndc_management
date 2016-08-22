#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

'''
    生成zabbix 的hostlist模板
'''
import sys
import os
sys.path.append('E:/GitWorkspace/enndc_management')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enndc_management.settings")
import django
django.setup()
import xlwt
from vmserver.models import *


font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.colour_index = 2
font0.bold = True

style0 = xlwt.XFStyle()
style0.font = font0

wb = xlwt.Workbook()
ws = wb.add_sheet('hostlist')
head = [u'主机名称', u'显示名', u'IP地址', u'分组名称', u'模板名称', u'主机位置',]
cloumn = 0
for header in head:
    ws.write(0, cloumn, header, style0)
    cloumn += 1

servers = List.objects.all()

row = 1
for server in servers:
    list_name = server.list_name
    hostname = server.hostname
    ip = server.ip
    group = server.os
    if group == 'linuxGuest':
        template = 'Template OS Linux'
    elif group == 'windowsGuest':
        template = 'Template OS Windows'
    else:
        template = ''
    location = u'虚拟机'
    ws.write(row, 0, hostname)
    ws.write(row, 1, list_name)
    ws.write(row, 2, ip)
    ws.write(row, 3, group)
    ws.write(row, 4, template)
    ws.write(row, 5, location)
    row += 1

wb.save('host_list.xls')
