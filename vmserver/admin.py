from django.contrib import admin

# Register your models here.
from vmserver import models

class ListAdmin(admin.ModelAdmin):
    list_display = (
        'list_name', 'ip', 'os', 'cpu', 'mem', 'total_hard_disk',
        'guest_status', 'app_name', 'app_role', 'vc',
    )
    list_filter = ('os', 'tools_status', 'guest_status', 'vc', 'esxi_host')
    readonly_fields = (
        'instance_uuid', 'list_name', 'hostname', 'ip', 'os', 'os_version', 'template',
		'cpu', 'mem', 'total_hard_disk', 'tools_status', 'guest_status', 'power_status',
		'esxi_host', 'vc', 'born_time',
    )
    search_fields = (
        'hostname', 'ip', 'os', 'os_version', 'cpu', 'mem', 'total_hard_disk',
        'tools_status', 'guest_status', 'vc', 'list_name', 'instance_uuid',
        'app_name'
    )
admin.site.register(models.List, ListAdmin)
