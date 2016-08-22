#!/usr/bin/env python
# coding:utf-8
__author__ = 'sunyaxiong'

from django.shortcuts import render

def index(request):
    return render(request, 'base.html')

def dashboard(request):
    return render(request, 'vmserver/dashboard.html')