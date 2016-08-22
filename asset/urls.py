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
from django.conf.urls import include, url


from rest_framework import routers
from asset import view2 as views
from asset import views as asset_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'group', views.GroupViewSet)
router.register(r'host', views.HostViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'maintenance', views.MaintenanceViewSet)

urlpatterns = [

    #url(r'^list/$', cmdb_views.list),
    #url(r'^server/(?P<sid>\d{1,4})', cmdb_views.server_detail),
    #url(r'add_server/$', cmdb_views.add_server),
    #url(r'^detail/$', cmdb_views.server_detail_blank),
    # url(r'^server/', cmdb_views.server_info)

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^up/$', asset_views.add_server),
]
