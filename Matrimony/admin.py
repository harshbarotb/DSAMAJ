from django.contrib import admin
from .models import *

# Register your models here.


class MatrimonyUserRegAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'Cast', 'Email', 'HeadPerson', 'Degree', 'Study_Details', 'DOB', 'Age', 'Father_PhoneNo', 'Gender', 'Looking_For',
                       'Native_City', 'Current_City')
    fieldsets = (
        (None, {
            'fields': ('First_Name', 'Last_Name', 'Cast', 'Email', 'HeadPerson', 'Degree', 'Study_Details', 'Password',
                       'Confirm_Pass', 'DOB', 'Age', 'Father_PhoneNo', 'Height', 'Weight', 'Gender', 'Looking_For',
                       'Hobbies', 'Native_City', 'Current_City')

        }),
    )


admin.site.register(MatrimonyUserReg, MatrimonyUserRegAdmin)
