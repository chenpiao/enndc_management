#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'


from django import forms
from vmserver.models import List


class UpdateMangeInfoForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('app_name', 'app_role', 'app_description', 'app_admin', 'industry_group')
