#!/usr/bin/env python
# coding:utf-8
__author__ = 'sunyaxiong'

from django.shortcuts import render

def report(request):
    return render(request, 'report/report.html')
'''
def list():
    runner = ansible.runner.Runner(
        module_name='ping',
        module_args='',
        pattern='10.1.201.47',
        forks='10'
    )
    data = runner.run()
    return data

if __name__ == '__main__':

    list()
'''