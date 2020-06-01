from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
def Familyentry(request):
    familycodes = FamilyCode.objects.all()
    return render(request, 'UserEntry/RegForm.html', {'familycodes': familycodes})


def Fcode(request):
    familycodes = FamilyCode.objects.all()
    if request.method == "POST":
        Fcode = request.POST.get("Fcode")
        fcode = FamilyCode(F_Code=Fcode)
        fcode.save()
        return render(request, 'UserEntry/RegForm.html', {'familycodes': familycodes})
    else:
        return render(request, 'UserEntry/RegForm.html', {'familycodes': familycodes})


def Form_Submission(request):
    familycodes = FamilyCode.objects.all()
    if request.method == "POST":
        print("Value Submitted")
        print("Value Submitted")
        try:
            file = request.FILES["profile_image"]
            fs = FileSystemStorage()
            profile_image = fs.save(file.name, file)
            Fcode = request.POST.get('Fcode')
            zone = request.POST.get("zone")
            native_city = request.POST.get("native_city")
            mosaad = request.POST.get("mosaad")
            head_name = request.POST.get("head_name")
            father = request.POST.get("father")
            mother = request.POST.get("mother")
            grandfather = request.POST.get("grandfather")
            address = request.POST.get("address")
            town_name = request.POST.get("town_name")
            taluko = request.POST.get("taluko")
            district = request.POST.get("district")
            pincode = request.POST.get("pincode")
            phone_office = request.POST.get("phone_office")
            phone_home = request.POST.get("phone_home")
            email = request.POST.get("email")
            family = FamilyHead(Zone_Name=zone, Native_City=native_city, Mosad_City=mosaad, profile_image=profile_image,
                                HeadPerson_Of_Family=head_name, Father_Name=father, Mother_Name=mother,
                                F_Code=Fcode, GrandFather_Name=grandfather, Address=address, Town=town_name,
                                Taluko=taluko,
                                District=district,
                                CITY_PINCODE=pincode, Phone_NO_Office=phone_office, Phone_NO_Home=phone_home,
                                Email=email)
            family.save()
            Mem_Name = request.POST.getlist('M_Name[]')
            Mem_Rel = request.POST.getlist('M_Relation_To_Head[]')
            M_BOD = request.POST.getlist('M_BOD[]')
            M_Study_Qualifications = request.POST.getlist('M_Study_Qualifications[]')
            M_Profession = request.POST.getlist('M_Profession[]')
            M_Marital_Status = request.POST.getlist('M_Marital_Status[]')
            M_Blood_Group = request.POST.getlist('M_Blood_Group[]')
            M_Phone_NO = request.POST.getlist('M_Phone_NO[]')
            M_Sex = request.POST.getlist('M_Sex[]')
            F_Code = request.POST.getlist('F_Code[]')
            for Member, mem_rel, mem_bod, m_study_qualifications, m_profession, m_marital_status, m_blood_group, m_phone_no, m_sex, f_code in zip(
                    Mem_Name, Mem_Rel, M_BOD, M_Study_Qualifications, M_Profession, M_Marital_Status, M_Blood_Group,
                    M_Phone_NO,
                    M_Sex, F_Code):
                Mem_Details = FamilyMember(M_Name=Member,
                                           M_Relation_To_Head=mem_rel,
                                           M_BOD=mem_bod, M_F_Code=f_code,
                                           M_Study_Qualifications=m_study_qualifications,
                                           M_Profession=m_profession,
                                           M_Marital_Status=m_marital_status,
                                           M_Blood_Group=m_blood_group,
                                           M_Phone_NO=m_phone_no, M_Sex=m_sex)
                messages.success(request, "Added Successfully")
                Mem_Details.save()
                FamilyHeadFamilyMember = FamilyHeadFamilyMembers(family_M_id=Mem_Details, family_H_id=family)
                FamilyHeadFamilyMember.save()
        except Exception as e:
            print(e)
            messages.error(request, "Failed to Add Student")

        return render(request, 'UserEntry/RegForm.html', {'familycodes': familycodes})
    else:
        return HttpResponse("<h2>Method Now Allowed</h2>")


def LoginUser(request):
    if request.user == None or request.user == "" or request.user.username == "":
        return render(request, "UserEntryLogIn.html")
    else:
        return render(request, 'UserEntryLogIn.html')


def LogInPage(request):
    return render(request, 'UserEntry/UserEntryLogIn.html')


def DoLoginUser(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        login(request, user)
        if user != None:
            return HttpResponseRedirect('/Familyentry/')
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect('/LogInPage/')
    else:
        return HttpResponse("<h2>Method Not Allowed")
