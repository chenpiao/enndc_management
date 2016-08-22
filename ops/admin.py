#!usr/bin/env python
# coding:utf-8
from django.contrib import admin
from ops import models
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class HostInfoAdmin(admin.ModelAdmin):
	list_display = ('hostname', 'ip', 'app_name', 'datacenter_address', 'manage_ip')
	search_fields = ('hostname', 'ip', 'datacenter_address', 'type', 'OS', 'app_name', 'app_description', 'manage_ip')
	list_filter = ('datacenter_address', 'type', 'OS', 'manage_ip')
	raw_id_fields = ('sn', )
	actions_on_top = True
	actions_on_bottom = False


class VMServerAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ip', 'os', 'app_name', 'app_role', 'info_status')
    search_fields = ('hostname', 'ip', 'app_name', 'app_role', 'app_description')
    raw_id_fields = ('admin_con', )
    # radio_fields = {'OS': admin.VERTICAL}
    # actions = [copy]
    actions_on_top = True
    actions_on_bottom = False
    # fields = ('hostname', 'OS', 'ip')  控制字段显隐
    list_filter = ('type', 'os', 'pool_id', 'industry_groupName')  # 筛选控制器

    # 函数可作为admin的显示字段，需要添加到listdisplay
    def info_status(self, obj):
        if obj.delete_time:
            return u'<span style="color:red;font-weight:bold">%s</span>' % (u"已删除",)
        else:
            return u'<span style="color:green;font-weight:bold">%s</span>' % (u"正常",)

    info_status.short_description = u'状态'
    info_status.allow_tags = True
    '''
	fieldsets = [
        (
            '管理信息', {
                'fields': [
                    'hostname', 'ip', 'app_name', 'app_role', 'app_description', 'type', 'cluster',
                    'pool_id', 'domain', 'create_time', 'delete_time', 'industry_groupName',
                ],
                'classes': [
                    'suit-tab', 'suit-tab-manage'
                ]
            }
        )
    ]
    suit_form_tabs = (('manage', '管理信息'), ('config', '配置信息'))
    suit_form_includes = (
        #('asset/serverdetail.html', 'top', 'config'),
    )
	'''

class VspherePoolAdmin(admin.ModelAdmin):
    list_display = ('pool_name', 'pool_id', 'pool_desc')
    actions_on_top = True
    actions_on_bottom = False

class ContactAdmin(admin.ModelAdmin):
	search_fields = ('name', 'cn_name', 'phone', 'mail')
	list_display = ('name', 'cn_name', 'phone', 'mail')

# 注册数据库
# admin.site.register(models.UserInfo, UserInfoAdmin)
admin.site.register(models.VMServer, VMServerAdmin)
admin.site.register(models.HostInfo, HostInfoAdmin)
admin.site.register(models.VspherePool, VspherePoolAdmin)
admin.site.register(models.Contact, ContactAdmin)



'''
# actions = [函数名] 加入到models类中，实现批量下拉操作
def server_copy(modeladmin, request, queryset):
    queryset.update(status='p')
    server_copy.short_description = "批量执行动作"


class SeverStateFilter(admin.SimpleListFilter):
        title = (u'状态')
        parameter_name = 'del_status'

        def lookups(self, request, model_admin):

            return (
                (0, u'正常'),
                (1, u'已删除'),
            )

        def queryset(self, request, queryset):
            if self.value():
                if int(self.value()) == 0:
                    return queryset.filter()
                if int(self.value()) == 1:
                    return queryset.filter()
'''
