# coding:utf8
from django.shortcuts import render, render_to_response
from redis_conn import RedisDatabase
import json
from asset.models import *


def list(request):
    return render(request, 'asset/serverlist.html', {'list': Host.objects.all()})

def server_detail(request, sid):
    ip = request.POST['ip']
    server_info1 = Host.objects.get(id=sid)
    a = 'ansible_facts10.1.201.47'
    # ans_info = RedisDatabase.get_key(a)
    r = RedisDatabase()
    ans_info = r.get_value(a)
    return render_to_response('asset/serverdetail.html', {'server': server_info1,
                                                          'ans_info': json.dumps(ans_info),
                                                          }
                              )

def add_server(request):
    op = request.POST.get("op_name")
    print op
    return

def server_detail_blank(request):
    return render(request, 'asset/serverdetail.html')