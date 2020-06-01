from django.contrib import admin
from .models import *


# Register your models here.
class MagazineUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'Magazine_Cover_Page', 'Magazine_Cover_Title', 'Date')


admin.site.register(MagazineUpload, MagazineUploadAdmin)


class EventSectionAdmin(admin.ModelAdmin):
    list_display = ('id','Event_Cover_Title', 'Date')


admin.site.register(EventSection, EventSectionAdmin)


class EventImagesAdmin(admin.ModelAdmin):
    list_display = ('id',  'Upload_Image', 'Date')


admin.site.register(EventImages, EventImagesAdmin)


class EventCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'Event_Id', 'Date')


admin.site.register(EventCode, EventCodeAdmin)
