#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

import sys
import os
sys.path.append('E:\GitWorkspace\enndc_management')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enndc_management.settings")
import django
django.setup()

from asset.models import Host, HostLog, NetworkDevice, NetworkDeviceLog, Storage, StorageLog


def create_log_obj():
    data = Storage.objects.all()
    for obj in data:
        StorageLog.objects.create(
            sn_id=obj.sn,
        )

def sync_status():
    data = Storage.objects.all()
    for obj in data:
        log_obj = StorageLog.objects.get(sn_id=obj.sn)
        log_obj.peo = 'admin'
        log_obj.op = 'admin'
        log_obj.notes = 'sync_status'
        log_obj.state = obj.state
        log_obj.save()

if __name__ == '__main__':
    # create_log_obj()
    sync_status()
