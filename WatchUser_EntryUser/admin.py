from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(FeMale)
admin.site.register(Male)


class FamilyCodeAdmin(admin.ModelAdmin):
    list_display = ('Family_Code', 'Date')
    fieldsets = (
        (None, {
            'fields': ('Family_Code', 'Date')
        }),
    )


admin.site.register(FamilyCode, FamilyCodeAdmin)


class ZoneCodeAdmin(admin.ModelAdmin):
    list_display = ('ZoneName', 'ZoneCode', 'Family_Code')
    fieldsets = (
        (None, {
            'fields': ('ZoneName', 'ZoneCode', 'Family_Code')
        }),
    )


admin.site.register(ZoneCode, ZoneCodeAdmin)


class HeadPersonAdmin(admin.ModelAdmin):
    list_display = (
        'Family_Code', 'Native_City', 'HeadPerson_Of_Family', 'gender', 'Age', 'CURRENT_CITY',
        'Phone_NO', 'Email', 'Date', 'Zone_Name')
    fieldsets = (
        (None, {
            'fields': ('Zone_Name', 'Zone_Code', 'Family_Code', 'Native_City', 'HeadPerson_Of_Family', 'gender', 'Age',
                       'CURRENT_CITY', 'Phone_NO', 'Email', 'Date')
        }),
    )


admin.site.register(HeadPerson, HeadPersonAdmin)
