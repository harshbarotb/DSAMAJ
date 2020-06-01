from django.contrib import admin
from .models import *


# Register your models here.


class FamilyHeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'F_Code', 'HeadPerson_Of_Family', 'Zone_Name', 'Father_Name', 'Native_City', 'Town')


admin.site.register(FamilyHead, FamilyHeadAdmin)


class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'M_Name', 'M_F_Code', 'M_Marital_Status', 'M_Sex', 'M_Relation_To_Head', 'M_Phone_NO')


admin.site.register(FamilyMember, FamilyMemberAdmin)


class FamilyCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'F_Code')


admin.site.register(FamilyCode, FamilyCodeAdmin)


class FamilyHeadFamilyMembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'family_M_id', 'family_H_id', 'created_at')


admin.site.register(FamilyHeadFamilyMembers, FamilyHeadFamilyMembersAdmin)
