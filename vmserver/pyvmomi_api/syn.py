#!usr/bin/env python
# coding:utf-8

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


# info = VMServer.objects.all().values(
#    'hostname', 'admin_con', 'industry_groupName', 'app_name', 'app_role', 'app_description'
# )

info = []
all_vm = VMServer.objects.filter(delete_time=None)
for vm in all_vm:
    short_name = vm.hostname
    fqdn_name = vm.hostname + '.addom.xinaogroup.com'
    industry_obj = IndustryGroup.objects.get(name=vm.industry_groupName)
    try:
        admin_obj = Contact.objects.get(name=vm.admin_con)
    except Exception, e:
        print '{0} contact error'.format(vm.admin_con)

    try:
        obj = List.objects.get(hostname=short_name)
    except Exception, e:
        # print '{0} list error'.format(short_name)
        try:
            obj = List.objects.get(hostname=fqdn_name)
        except Exception, e:
            # print 'fqdn {0} list error'.format(fqdn_name)
            try:
                obj = List.objects.get(list_name=short_name)
            except Exception, e:
                print 'list_name {0} error'.format(short_name)
    finally:
        obj.app_name = vm.app_name
        obj.app_role = vm.app_role
        obj.app_description = vm.app_description
        obj.app_admin = admin_obj
        obj.industry_group = industry_obj
        obj.save()
