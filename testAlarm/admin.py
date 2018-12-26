from django.contrib import admin
from testAlarm.models import DevID, Image


class DevIDAdmin(admin.ModelAdmin):
    list_display = ['devid', 'name']
    search_fields = ['devid']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['type', 'picture']
    search_fields = ['type']


admin.site.register(DevID, DevIDAdmin)
admin.site.register(Image, ImageAdmin)

