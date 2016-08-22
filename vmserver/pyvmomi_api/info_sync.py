#!usr/bin/env python
# coding:utf-8

'''
测试模块---该模块用来同步手工表VMServer和自动表List的管理信息（管理员、归属公司等）
'''

__author__ = 'sunyaxiong'

import sys
import os
sys.path.append('E:/GitWorkspace/enndc_management')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enndc_management.settings")
import django
django.setup()
from ops.models import VMServer, Contact
from vmserver.models import List
from asset.models import IndustryGroup
import datetime
import pprint

# 手工表VMServer中取出信息
info = VMServer.objects.filter(delete_time=None).values(
    'hostname', 'admin_con', 'industry_groupName', 'app_name', 'app_role', 'app_description'
)
# pprint.pprint(info)
print len(info)

vm_list = []
print datetime.datetime.now()
for i in info:
    short_name = i['hostname']
    industry = i['industry_groupName']
    admin_con = i['admin_con']
    try:
        admin_obj = Contact.objects.get(name=admin_con)
    except Exception, e:
        print 'not found: ', admin_con
    industry_obj = IndustryGroup.objects.get(name=industry)
    vm_list.append(i['hostname'])
    # print len(vm_list)
    auto_list = List.objects.filter(template='False')
    for list_obj in auto_list:
        hostname = list_obj.hostname
        if hostname is None:  # hostname有为空的情况，需要排除
            # print list_obj
            continue
        hostname = hostname.split('.')[0]
        dy = 0
        if list_obj.list_name == short_name:
            dy += 1
        if hostname == short_name:
            dy += 1
        if dy == 0:
            pass
        else:
            list_obj.app_name = i['app_name']
            list_obj.app_role = i['app_role']
            list_obj.app_description = i['app_description']
            list_obj.app_admin = admin_obj
            list_obj.industry_group = industry_obj
            list_obj.save()

print 'len', len(vm_list)
print datetime.datetime.now()
