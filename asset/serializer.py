#!/usr/bin/env python
# coding:utf-8
__author__ = 'syx'

# from django.core import serializers
import sys
import os
sys.path.append('D:/svn/Openstack/SourceCode/CMDB/enndc_management')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enndc_management.settings")
from asset import models
from django.contrib.auth.models import User
from rest_framework import serializers
from asset.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

'''
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
'''

class HostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Host
        fields = ('sn', 'type', 'vendor', 'product_model', 'ownership', 'maintenance_group_name')
        extra_kwargs = {
            'url': {'ownership': 'maintenance_group_name'},
            'users': {'lookup_field': 'type'}
        }

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = IndustryGroup
        fields = ('name',)

class MaintenanceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Maintenance
        fields = ('maintenance_group', 'maintenance_contact', 'maintenance_phone')