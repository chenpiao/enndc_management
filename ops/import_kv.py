#!/usr/bin/python
# coding:utf8

import sys
import os
sys.path.append('E:/GitWorkspace/enndc_management')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enndc_management.settings")
from ops.models import VMServer
# from openpyxl import Workbook
# from openpyxl import load_workbook
import json
import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='dbuser',
    passwd='Enndc@',
    db='enndc',
)
cur = conn.cursor()

'''
wb = load_workbook(filename='D:\Users\sunyaxiong\Desktop\dd.xlsx')
ws = wb['key']  # ws is now an IterableWorksheet
ws2 = wb['value']
a = []
b = []
for row in ws.rows:
	for cell in row:
        a.append(cell.value)
for row2 in ws2.rows:
	for cell2 in row2:
        b.append(cell2.value)

d = dict(zip(a, b))
json.dump(d, open('kv.txt', 'w'))
'''

c = json.load(file('kv.txt'))

'''
for i in c.keys():
	p = VMServer.objects.get(hostname=i)
	p.admin_con = c.get(i, 'not found')
	print p.admin_con
	#p.save() 
'''
for i in c.keys():
	sqli='update ops_vmserver SET admin_con_id="%s" WHERE hostname="%s"'%(c.get(i), i)
	print sqli
	cur.execute(sqli)

cur.close()
conn.commit()
conn.close()