#!usr/bin/env python
# coding:utf-8
from django.contrib import admin
from asset import models


class HostInline(admin.TabularInline):
    model = models.HostLog
    readonly_fields = ('state', 'peo', 'phone', 'op', 'notes', 'update_time')
    fields = ('state', 'peo', 'phone', 'op', 'notes', 'update_time')
    # raw_id_fields = ('op', )
    suit_classes = 'inline-group suit-tab suit-tab-general show'

class NetworkDeviceInline(admin.TabularInline):
    model = models.NetworkDeviceLog
    readonly_fields = ('state', 'peo', 'phone', 'op', 'notes', 'update_time')
    fields = ('state', 'peo', 'phone', 'op', 'notes', 'update_time')
    # raw_id_fields = ('op', )
    suit_classes = 'inline-group suit-tab suit-tab-general show'

class StorageInline(admin.TabularInline):
    model = models.StorageLog
    readonly_fields = ('state', 'peo', 'phone', 'op', 'notes', 'update_time')
    fields = ('state', 'peo', 'phone', 'op', 'notes', 'update_time')
    # raw_id_fields = ('op', )
    suit_classes = 'inline-group suit-tab suit-tab-general show'

class HostAdmin(admin.ModelAdmin):
    inlines = (HostInline,)
    raw_id_fields = ('maintenance_group_name',)
    readonly_fields = ('born_time', )
    list_display = ('sn', 'type', 'product_model', 'vendor', 'status', 'idc', 'zone', 'cabinet', 'unit_start', 'unit_end', 'power', 'born_time')
    search_fields = ('sn', 'type', 'product_model', 'vendor', 'product_model')
    list_filter = ('type', 'vendor', 'idc', 'status', 'zone', 'cabinet')
    fieldsets = [
        ('基础资产信息', {'fields':
                        ['type', 'vendor', 'product_model', 'sn', 'be_from', 'ownership', 'purchase_date',
                         'idc', 'zone', 'cabinet', 'unit_start', 'unit_end', 'power', 'status', 'maintenance_date',
                         'maintenance_group_name'],
                         'classes': ['suit-tab', 'suit-tab-general']
                    }
         ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                'classes': ['suit-tab', 'suit-tab-general']
            }
        ),
    ]
    suit_form_tabs = (('general', '基础信息'), ('log', '资产状态变更'), ('config', '资产配置'))
    suit_form_includes = (
        # ('asset/host_tag/host_status_action.html', 'top', 'log'),
        # ('asset/maintenance_log_table.html', 'bottom', 'log'),
    )

class NetworkDeviceAdmin(admin.ModelAdmin):
    inlines = (NetworkDeviceInline, )
    list_display = ('type', 'vendor', 'product_model', 'sn', 'be_from', 'idc', 'zone', 'cabinet', 'unit_start', 'unit_end', 'born_time')
    search_fields = ('type', 'vendor', 'product_model', 'sn', 'be_from', 'branch')
    readonly_fields = ('born_time', )
    list_filter = ('type', 'be_from', 'status', 'branch', 'idc', 'zone', 'cabinet')
    fieldsets = [
        ('基础资产信息', {'fields':
                        ['type', 'vendor', 'product_model', 'sn', 'be_from', 'ownership', 'purchase_date', 'contract',
                        'idc', 'branch', 'zone', 'cabinet', 'unit_start', 'unit_end', 'status', 'power', 'maintenance_date',
                         'maintenance_group'],
                        'classes': ['suit-tab', 'suit-tab-general']
                    }
        ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                'classes': ['suit-tab', 'suit-tab-general']
            }
        )
    ]
    suit_form_tabs = (('general', '基础信息'), ('log', '资产状态变更'))
    suit_form_includes = (
        # ('asset/maintenance_log_table.html', 'bottom', 'maintenance'),
    )

class NetworkDeviceLogAdmin(admin.ModelAdmin):
    raw_id_fields = ('sn',)
    list_display = ('get_sn', 'state', 'op', 'peo', 'phone', 'update_time')
    search_fields = ('state', 'op', 'peo')
    readonly_fields = ('op', 'born_time')

    def save_model(self, request, obj, form, change):
        obj.op = request.user
        obj.save()

    def get_sn(self, obj):

        return u'%s' % obj.sn_id

class StorageAdmin(admin.ModelAdmin):
    inlines = (StorageInline, )
    list_display = ('sn', 'manufacturers', 'device_type', 'product_model', 'ownership', 'contract', 'idc', 'zone', 'cabinet',
                    'unit_start', 'unit_end', 'born_time')
    search_fields = ('device_type', 'product_model', 'manufacturers', 'sn', 'be_from', 'contract')
    readonly_fields = ('born_time', )
    list_filter = ('device_type', 'product_model', 'be_from', 'ownership', 'idc', 'zone', 'cabinet')
    fieldsets = [
        (
            '资产基础信息', {
                'fields': [
                    'device_type', 'manufacturers', 'product_model', 'sn', 'be_from', 'ownership', 'purchase_date',
                    'contract', 'disk_num', 'disk_model', 'disk_fru', 'fsp_num', 'ext_fsp_num', 'power_num',
                    'idc', 'zone', 'cabinet', 'unit_start', 'unit_end', 'state', 'maintenance_date',
                    'maintenance_group',
                ],
                'classes': [
                    'suit-tab', 'suit-tab-general'
                ]
            }
        ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                'classes': ['suit-tab', 'suit-tab-general']
            }
        )
    ]
    suit_form_tabs = (('general', '基础信息'), ('log', '资产状态变更'))
    suit_form_includes = (
        #('asset/maintenance_log_table.html', 'bottom', 'maintenance'),
    )

class StorageLogAdmin(admin.ModelAdmin):
    raw_id_fields = ('sn',)
    list_display = ('get_sn', 'state', 'op', 'peo', 'phone', 'update_time')
    search_fields = ('state', 'op', 'peo')
    readonly_fields = ('op', 'born_time')

    def save_model(self, request, obj, form, change):
        obj.op = request.user
        obj.save()

    def get_sn(self, obj):

        return u'%s' % obj.sn_id

class TapeAdmin(admin.ModelAdmin):
    list_display = ('host', 'device_type', 'product_model', 'content', 'sn', 'be_from', 'ownership', 'manufacturers', 'born_time')
    search_fields = ('device_type', 'product_model', 'sn', 'content', 'be_from', 'manufacturers', 'ownership__name')
    list_filter = ('device_type', 'product_model', 'be_from')
    readonly_fields = ('born_time', )
    raw_id_fields = ('host',)
    fieldsets = [
        (
            '资产基础信息', {
                'fields': [
                    'host', 'device_type', 'product_model', 'sn', 'content', 'be_from', 'ownership', 'purchase_date',
                    'manufacturers', 'contract', 'strongbox', 'tape_library_name', 'state'
                ],
                'classes': [
                    'suit-tab', 'suit-tab-general'
                ]
            }
        ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                'classes': ['suit-tab', 'suit-tab-general']
            }
        )
    ]
    suit_form_tabs = (('general', '基础信息'),)
    suit_form_includes = (
        #('asset/maintenance_log_table.html', 'bottom', 'maintenance'),
    )

class ToolsAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'part_No', 'amount', 'inventory_num', 'color', 'size', 'be_from',
                    'ownership', 'born_time')
    list_filter = ('device_type', 'be_from', 'part_No')
    search_fields = ('device_type', 'be_from', 'part_No')
    readonly_fields = ('born_time',)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('type', 'product_model', 'sn', 'amount', 'size', 'be_from', 'purchase_date', 'born_time')
    search_fields = ('type', 'product_model', 'size', 'be_from')
    readonly_fields = ('born_time', )
    list_filter = ('type', 'be_from')
    fieldsets = [
        ('基础资产信息', {'fields':
                        ['type', 'product_model', 'sn', 'amount', 'size', 'be_from', 'ownership', 'purchase_date',
                         'vendor', 'contract', 'location', 'using_status', 'maintenance_date', 'maintenance_section',
                         'abandon_time'],
                        # 'classes': ['suit-tab', 'suit-tab-general']
                    }
         ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                # 'classes': ['suit-tab', 'suit-tab-general']
            }
        )
    ]

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'number', 'be_from', 'purchase_date', 'vendor', 'born_time')
    search_fields = ('name', 'version', 'number', 'be_from', 'purchase_date', 'vendor')
    readonly_fields = ('born_time', )
    fieldsets = [
        ('基础资产信息', {'fields':
                        ['name', 'version', 'number', 'be_from', 'purchase_date', 'vendor', 'contract', 'related_app',
                         'user_name', 'user_phone', 'user_email', 'use_status', 'maintenance_date'],
                        # 'classes': ['suit-tab', 'suit-tab-general']
                    }
         ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                # 'classes': ['suit-tab', 'suit-tab-general']
            }
        )
    ]

class IndustryGroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
    readonly_fields = ('born_time',)

class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('maintenance_group', 'maintenance_contact', 'maintenance_phone', 'born_time')
    search_fields = ('maintenance_group', 'maintenance_contact', 'maintenance_phone')
    readonly_fields = ('born_time',)

class HostLogAdmin(admin.ModelAdmin):
    raw_id_fields = ('sn',)
    list_display = ('get_sn', 'state', 'op', 'peo', 'phone', 'update_time')
    search_fields = ('state', 'op', 'peo')
    readonly_fields = ('op', 'born_time')

    def save_model(self, request, obj, form, change):
        obj.op = request.user
        obj.save()

    def get_sn(self, obj):

        return u'%s' % obj.sn_id

class HostSparePartAdmin(admin.ModelAdmin):
    list_display = ('host', 'sn', 'type', 'model', 'vendor', 'born_time')
    readonly_fields = ('born_time',)
    raw_id_fields = ('host', )

class NetworkSparePartAdmin(admin.ModelAdmin):
    list_display = ('host', 'sn', 'type', 'pro_model', 'vendor', 'born_time')
    search_fields = ('sn', 'type', 'vendor')
    list_filter = ('type', 'vendor')
    readonly_fields = ('born_time', )
    raw_id_fields = ('host', )

class StorageSparePartAdmin(admin.ModelAdmin):
    list_display = ('host', 'sn', 'model', 'vendor', 'capacity')
    search_fields = ('sn', 'model', 'vendor', 'capacity')
    list_filter = ('model', 'vendor')
    raw_id_fields = ('host', )

admin.site.register(models.Host, HostAdmin)
admin.site.register(models.HostLog, HostLogAdmin)
admin.site.register(models.NetworkDevice, NetworkDeviceAdmin)
admin.site.register(models.NetworkDeviceLog, NetworkDeviceLogAdmin)
admin.site.register(models.Storage, StorageAdmin)
admin.site.register(models.StorageLog, StorageLogAdmin)
admin.site.register(models.Tape, TapeAdmin)
admin.site.register(models.Tools, ToolsAdmin)
admin.site.register(models.Equipment, EquipmentAdmin)
admin.site.register(models.Software, SoftwareAdmin)
admin.site.register(models.IndustryGroup, IndustryGroupAdmin)
admin.site.register(models.Maintenance, MaintenanceAdmin)
admin.site.register(models.HostSparePart, HostSparePartAdmin)
admin.site.register(models.NetworkSparePart, NetworkSparePartAdmin)
admin.site.register(models.StorageSparePart, StorageSparePartAdmin)
# admin.site.register(models.DataCenter, DataCenterAdmin)
# admin.site.register(models.Zone, ZoneAdmin)
# admin.site.register(models.RackUnit, RackUnitAdmin)
