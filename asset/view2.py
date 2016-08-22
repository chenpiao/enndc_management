#!/usr/bin/env python
# coding:utf-8
__author__ = 'syx'

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from asset.serializer import UserSerializer, HostSerializer, GroupSerializer, MaintenanceSerializer
from asset.models import *



class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
'''
class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
'''
class HostViewSet(viewsets.ModelViewSet):

    # lookup_field = ('maintenance_group',)
    queryset = Host.objects.all()
    serializer_class = HostSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MaintenanceViewSet(viewsets.ModelViewSet):

    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
