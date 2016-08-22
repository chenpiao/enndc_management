"""enndc_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^dashboard_190/$', views.vc_overview),
    url(r'^dashboard_101/$', views.vc_overview_101),
    url(r'^dashboard_151/$', views.vc_overview_151),
    url(r'^vms/$', views.vms),
    url(r'^update_manage_info/$', views.update_manage_info),
    url(r'^vms/(?P<sid>\d{1,9})', views.vm_detail),
    url(r'^vc', views.vms_vc),
    url(r'^hosts', views.host_info),

    url(r'^reports/offline_check/$', views.offline_check),
    url(r'^reports/info_missing/$', views.info_missing_report),

    url(r'^export_all_vms', views.excel_view),

    url(r'^command_excute', views.command_excute),
    url(r'^return_value', views.return_value),
]
