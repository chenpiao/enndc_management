#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

'''
    该脚本用来导出zabbix服务器所有host的name、ip、group信息到同目录下的excel
'''

import sys
import os
sys.path.append('E:\GitWorkspace\enndc_management')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enndc_management.settings")
import django
django.setup()
from pyzabbix import ZabbixAPI
from ops.models import Contact
from vmserver.models import List


url = 'http://10.37.4.97/zabbix'
user = 'admin'
pwd = 'zabbix'

class ZabbixExport(object):

    def __init__(self, url=url, user=user, pwd=pwd):
        try:
            self.zapi = ZabbixAPI(url)
            self.zapi.login(user, pwd)
        except:
            print '\n 登录zabbix平台出现错误'
            sys.exit()

    def get_info(self):

        # get the host info and insert to host_list
        # hosts = self.zapi.host.get(filter={'host': 'elcndc2bbmh02'})
        error_num = 0
        hosts = self.zapi.host.get()
        for host in hosts:
            hostid = host['hostid']
            print hostid
            try:
                vm_obj = List.objects.get(list_name=host['host'], delete_time=None, template='False')
                contact_obj = Contact.objects.get(name=vm_obj.app_admin_id)
            except Exception, e:
                print e
                print '{0} get has some error'.format(host['host'])
                error_num += 1
                continue
            # if host['host'] == 'elcndc2ekxx01t':
            data = {
                'location': vm_obj.vc,
                'os': vm_obj.os,
                'os_full': vm_obj.os_version,
                'poc_1_name': contact_obj.cn_name,
                'poc_1_email': contact_obj.mail,
                'poc_1_cell': contact_obj.phone,
                'poc_1_notes': vm_obj.app_description
            }
            self.zapi.host.update(hostid=hostid, inventory_mode=0, inventory=data)
        print len(hosts)
        print '出错主机数：{}'.format(error_num)

if __name__ == '__main__':
    zab = ZabbixExport()
    zab.get_info()
