#!usr/bin/env python
# coding:utf-8

from enndc_management.settings import *
from vmserver.tools import VCenterInfo, ParamikoAPI
from forms import UpdateMangeInfoForm
from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from vmserver.models import List, Contact
from asset.models import IndustryGroup
from django.db.models import Q
import json

def vc_overview(request):
    user = request.user
    data = {}
    vc_ip = '10.37.17.190'
    vc_name = VC_POOL[vc_ip]
    conn = VCenterInfo(vc_ip)
    vms= conn.vms_info()
    hosts = conn.hosts_info()
    data['vm_amount'] = len(vms)
    data['host_amount'] = len(hosts)
    vc_mem_per = conn.host_mem()
    hosts_list = conn.get_host_info()
    for host in hosts_list:
        host['cpu_percentage'] = float(host['cpu_usage']) / float(host['cpu_cores'] * host['cpu_mhz'])
        host['cpu_percentage'] = format(host['cpu_percentage'] * 100, '.2f')
        host['mem_percentage'] = host['mem_usage'] / float(host['mem'])
        host['mem_percentage'] = round(float(host['mem_percentage']) * 100, 2)
    return render_to_response(
        'vmserver/dashboard.html', {
            'data': data,
            'vc_ip': vc_ip,
            'vc_name': vc_name,
            'user': user,
            'vc_mem_per': vc_mem_per,
            'hosts': hosts_list
        }
    )

def vc_overview_101(request):
    user = request.user
    data = {}
    vc_ip = '10.37.17.101'
    vc_name = VC_POOL[vc_ip]
    conn = VCenterInfo(vc_ip)
    vms= conn.vms_info()
    hosts = conn.hosts_info()
    data['vm_amount'] = len(vms)
    data['host_amount'] = len(hosts)
    vc_mem_per = conn.host_mem()
    hosts_list = conn.get_host_info()
    for host in hosts_list:
        host['cpu_percentage'] = float(host['cpu_usage']) / float(host['cpu_cores'] * host['cpu_mhz'])
        host['cpu_percentage'] = format(host['cpu_percentage'] * 100, '.2f')
        host['mem_percentage'] = host['mem_usage'] / float(host['mem'])
        host['mem_percentage'] = round(float(host['mem_percentage']) * 100, 2)
    return render_to_response(
        'vmserver/dashboard.html', {
            'data': data,
            'vc_ip': vc_ip,
            'vc_name': vc_name,
            'user': user,
            'vc_mem_per': vc_mem_per,
            'hosts': hosts_list
        }
    )

def vc_overview_151(request):
    user = request.user
    data = {}
    vc_ip = '10.32.18.151'
    vc_name = VC_POOL[vc_ip]
    conn = VCenterInfo(vc_ip)
    vms= conn.vms_info()
    hosts = conn.hosts_info()
    data['vm_amount'] = len(vms)
    data['host_amount'] = len(hosts)
    vc_mem_per = conn.host_mem()
    hosts_list = conn.get_host_info()
    for host in hosts_list:
        host['cpu_percentage'] = float(host['cpu_usage']) / float(host['cpu_cores'] * host['cpu_mhz'])
        host['cpu_percentage'] = format(host['cpu_percentage'] * 100, '.2f')
        host['mem_percentage'] = host['mem_usage'] / float(host['mem'])
        host['mem_percentage'] = round(float(host['mem_percentage']) * 100, 2)
    return render_to_response(
        'vmserver/dashboard.html', {
            'data': data,
            'vc_ip': vc_ip,
            'vc_name': vc_name,
            'user': user,
            'vc_mem_per': vc_mem_per,
            'hosts': hosts_list
        }
    )

def vms(request):
    user = request.user
    servers = List.custom_objs.vms_all()
    return render_to_response(
        'vmserver/all_vms.html', {
            'list': servers,
            'user': user,
        }
    )

def excel_view(request):
    import xlwt

    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2
    font0.bold = True

    style0 = xlwt.XFStyle()
    style0.font = font0

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('vms')
    head = [
        '清单名', '主机名称', 'IP地址', 'OS类型', 'OS版本', 'CPU', '内存', '磁盘大小',
        '是否模板', '虚拟机状态', '电源状态', 'Tools状态', 'ESXI主机IP', 'VCenterIP',
        'app名称', 'app角色', 'app管理员', '归属公司'
    ]
    cloumn = 0
    for header in head:
        worksheet.write(0, cloumn, header, style0)
        cloumn += 1

    servers = List.objects.filter(delete_time=None)
    row = 1
    for server in servers:
        worksheet.write(row, 0, server.list_name)
        worksheet.write(row, 1, server.hostname)
        worksheet.write(row, 2, server.ip)
        worksheet.write(row, 3, server.os)
        worksheet.write(row, 4, server.os_version)
        worksheet.write(row, 5, server.cpu)
        worksheet.write(row, 6, server.mem)
        worksheet.write(row, 7, server.total_hard_disk)
        worksheet.write(row, 8, server.template)
        worksheet.write(row, 9, server.guest_status)
        worksheet.write(row, 10, server.power_status)
        worksheet.write(row, 11, server.tools_status)
        worksheet.write(row, 12, server.esxi_host)
        worksheet.write(row, 13, server.vc)
        worksheet.write(row, 14, server.app_name)
        worksheet.write(row, 15, server.app_role)
        worksheet.write(row, 16, server.app_admin_id)
        worksheet.write(row, 17, server.industry_group_id)
        row += 1
    response = HttpResponse(content_type='application/msexcel')
    response['Content-Disposition'] = 'attachment; filename=vms.xls'
    workbook.save(response)
    return response

def vms_vc(request):
    ip = request.GET['ip']
    user = request.user
    servers = List.objects.filter(vc=ip, delete_time=None)
    return render_to_response(
        'vmserver/all_vms.html', {
            'list': servers,
            'user': user,
        }
    )

def offline_check(request):
    user = request.user
    off_list = []
    all = List.objects.filter(template='false')
    for obj in all:
        if obj.delete_time:
            off_list.append(obj)
    return render_to_response(
        'vmserver/offline_vms.html', {
            'user': user,
            'off_list': off_list,

        }
    )

def vm_detail(request, sid):
    user = request.user
    page_head = '虚拟机详情'
    vm = List.objects.get(id=sid)
    users = Contact.objects.all()
    coms = IndustryGroup.objects.all()
    return render_to_response(
        'vmserver/serverdetail.html', {
            'vm': vm,
            'user': user,
            'page_head': page_head,
            'users': users,
            'coms': coms,
        }
    )

def info_missing_report(request):
    user = request.user
    vms = List.objects.filter(delete_time=None, template='False').filter(
        Q(app_name=None) | Q(app_role=None) | Q(app_description=None) | Q(app_admin=None) |
        Q(industry_group=None)
    )
    return render_to_response(
        'vmserver/info_missing.html', {
            'user': user,
            'vms': vms,
        }
    )

def update_manage_info(request):
    user = request.user
    if request.method == 'POST':
        uuid = request.POST.get('uuid')
        vm_obj = List.objects.get(instance_uuid=uuid)
        form = UpdateMangeInfoForm(request.POST, instance=vm_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vmserver/reports/info_missing/')
    else:
        form = UpdateMangeInfoForm()

    return HttpResponseRedirect('/vmserver/reports/info_missing/')

def host_info(request):
    ip = request.GET['ip']
    vc_name = VC_POOL[ip]
    user = request.user
    conn = VCenterInfo(ip)
    hosts_list = conn.get_host_info()
    for host in hosts_list:
        host['cpu_percentage'] = float(host['cpu_usage']) / float(host['cpu_cores'] * host['cpu_mhz'])
        host['cpu_percentage'] = format(host['cpu_percentage'], '.2%')
        host['mem_percentage'] = host['mem_usage'] / float(host['mem'])
        host['mem_percentage'] = format(float(host['mem_percentage']), '.2%')
        print host['mem_percentage']

    return render_to_response(
        'vmserver/host_info.html', {
            'user': user,
            'hosts': hosts_list,
            'vc_name': vc_name,
            'vc_ip': ip,
        }
    )

def command_excute(request):
    user = request.user
    list_name = request.GET['vm']
    print list_name
    ip = request.GET['ip']
    return render_to_response(
        'vmserver/command_excute.html', {
            'user': user,
            'list_name': list_name,
            'ip': ip,
        }
    )

def return_value(request):
    user = request.user
    if request.method == 'POST':
        hostname = request.POST.get('hostname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        command = request.POST.get('command')
        try:
            conn = ParamikoAPI(hostname=hostname, username=username, password=password)
            back_value = conn.excute_shell(command)
        except Exception, e:
            return HttpResponse(json.dumps(e.message))
        if back_value:
            return HttpResponse(json.dumps(back_value))
        else:
            message = '亲，命令不正确或者操作系统不支持该命令，远程执行功能暂时只能支持类Unix系统'
            return HttpResponse(json.dumps(message))
