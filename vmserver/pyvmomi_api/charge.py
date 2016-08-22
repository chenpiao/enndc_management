#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'
import datetime
from vmserver.models import List, ListInfoLog

day_price = {
    'cpu': 10,
    'mem': 20,
    'disk': 30
}

time_delta = datetime.date.today()

def charge():
    objs = List.objects.all()
    for obj in objs:
        cpu = obj.cpu
        mem = obj.mem
        disk = obj.total_hard_disk
        uuid = obj.instance_uuid
        if ListInfoLog.objects.get(vm_ins=uuid):
            pass
        else:
            day_price['cpu'] * cpu * 'tiem_delta'