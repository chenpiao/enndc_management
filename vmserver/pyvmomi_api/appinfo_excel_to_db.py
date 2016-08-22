#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
sys.path.append('E:/GitWorkspace/enndc_management/enndc_management')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django
django.setup()
from django.db.models import F, Count
from vmserver.models import List
from openpyxl import load_workbook
from enndc_management.settings import *
import pprint
import json
import logging


LOG = logging.getLogger('vmserver')
BUG = logging.getLogger('request')


def get_excel_info():
    wb = load_workbook(filename=BASE_DIR + '/vmserver/pyvmomi_api/info-lzc.xlsx')
    ws = wb['info']
    rows = ws.rows

    info_list = []
    for row in rows:
        info = {}
        for i in range(len(row)):
            info[rows[0][i].value] = row[i].value
        info_list.append(info)
    del info_list[0]
    # print len(info_list)
    # json.dump(info_list, open('info.json', 'w'), indent=4, ensure_ascii=False)
    return info_list

def compare_update():
    info_list = get_excel_info()
    successed_flag = 0
    failed_flag = 0
    for info in info_list:
        query = List.objects.filter(list_name=info['list_name'])
        if len(query) == 0:
            LOG.info('{0} not found'.format(info['list_name']))
            failed_flag += 1
        else:
            query.update(**info)
            LOG.info('vm {0} has updated'.format(info['list_name']))
            successed_flag += 1

    LOG.info('there has {0} vm info update and {1} vm info failed'.format(successed_flag, failed_flag))


if __name__ == '__main__':
    get_excel_info()
