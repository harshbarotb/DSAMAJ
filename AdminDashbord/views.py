from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from UserEntry.models import *
from HomePage.models import *
from Magazine.models import EventCode, EventSection, EventImages, MagazineUpload
from WatchUser_EntryUser.filters import HeadPersonFilter
import datetime


# Create your views here.


def CalCulateAge(request):
    td = datetime.datetime.now().date()
    members = FamilyMember.objects.all()
    memberlist = []
    for mem in members:
        bd = mem.M_BOD
        print(bd)
        age_years = int((td - bd).days / 365.25)
        memberlist.append({"model": model_to_dict(mem), 'age': age_years})

    print(memberlist)
    return render(request, 'AdminDashbord/CalculateAge.html', {'members': memberlist})


def BasicInfoHead(request):
    headpersons = FamilyHead.objects.all()
    male = FamilyMember.objects.filter(M_Sex='Male')
    Female = FamilyMember.objects.filter(M_Sex='FeMale')
    FeMale_Count = Female.count()
    Count_Male = male.count()
    Count_Family = headpersons.count()
    myFilter = HeadPersonFilter(request.GET, queryset=headpersons)
    headpersons = myFilter.qs
    return render(request, 'AdminDashbord/basic_InfoHead.html',
                  {'FeMale_Count': FeMale_Count, 'Count_Male': Count_Male, 'HeadPerson': headpersons,
                   'myFilter': myFilter, 'Count_Family': Count_Family})


def Dashboard(request):
    return render(request, 'AdminDashbord/base_admin.html')


def ShowFamily(request, head_id):
    Head = FamilyHead.objects.filter(id=head_id)
    Member = FamilyMember.objects.all()
    return render(request, 'AdminDashbord/Show_Family.html', {'Head': Head, 'member': Member})


def FemaleInfo(request):
    female = FamilyMember.objects.filter(M_Sex='FeMale')
    return render(request, 'AdminDashbord/FemaleMemberList.html', {'member': female})


def MaleInfo(request):
    male = FamilyMember.objects.filter(M_Sex='Male')
    return render(request, 'AdminDashbord/MaleMemberList.html', {'member': male})


def MemHeadData(request):
    familyCode = FamilyHead.objects.all()
    familymember = FamilyMember.objects.all()
    contex = {'head': familyCode, 'member': familymember}
    print(contex)
    return render(request, 'AdminDashbord/MemHeadData.html', contex)


def AddFamilyMemberfFirstPageDirection(request):
    familycodes = FamilyCode.objects.all()
    return render(request, 'AdminDashbord/AddExtraMember.html', {'familycodes': familycodes})


def AddExtraFamilyMember(request):
    familycodes = FamilyCode.objects.all()
    if request.method == "POST":
        print("Value Submitted")
        print("Value Submitted")
        try:
            Mem_Name = request.POST.get('M_Name')
            Mem_Rel = request.POST.get('M_Relation_To_Head')
            M_BOD = request.POST.get('M_BOD')
            M_Study_Qualifications = request.POST.get('M_Study_Qualifications')
            M_Profession = request.POST.get('M_Profession')
            M_Marital_Status = request.POST.get('M_Marital_Status')
            M_Blood_Group = request.POST.get('M_Blood_Group')
            M_Phone_NO = request.POST.get('M_Phone_NO')
            M_Sex = request.POST.get('M_Sex')
            F_Code = request.POST.get('F_Code')
            Mem_Details = FamilyMember(M_Name=Mem_Name,
                                       M_Relation_To_Head=Mem_Rel,
                                       M_BOD=M_BOD, M_F_Code=F_Code,
                                       M_Study_Qualifications=M_Study_Qualifications,
                                       M_Profession=M_Profession,
                                       M_Marital_Status=M_Marital_Status,
                                       M_Blood_Group=M_Blood_Group,
                                       M_Phone_NO=M_Phone_NO, M_Sex=M_Sex)
            messages.success(request, "Added Successfully")
            Mem_Details.save()
        except Exception as e:
            print(e)
            messages.error(request, "Failed to Add Student")
        return render(request, 'AdminDashbord/AddExtraMember.html', {'familycodes': familycodes})
    else:
        return HttpResponse("<h2>Method Now Allowed</h2>")


def DeleteHeadData(request, head_id):
    headData = FamilyHead.objects.get(id=head_id)
    headData.delete()
    messages.error(request, "Deleted Successfully")
    return HttpResponseRedirect("/FamilyHeadInfo")


def DeleteMemberData(request, member_id):
    memberData = FamilyMember.objects.get(id=member_id)
    memberData.delete()
    messages.error(request, "Deleted Successfully")
    return HttpResponseRedirect("/FamilyHeadInfo")


def EventImagesDashBoardHomePage(request):
    eventcode = EventCode.objects.all()
    return render(request, 'AdminDashbord/EventPhotosAndCoverPage.html', {'EventId': eventcode})


def EventCoverImagesPage(request):
    if request.method == 'POST':
        file = request.FILES["Event_Cover_Page"]
        fs = FileSystemStorage()
        Event_Cover_Page = fs.save(file.name, file)
        Event_Cover_Title = request.POST.get('Event_Cover_Title')
        Event_Id = EventCode.objects.get(Event_Id=request.POST.get('Event_Id'))
        Re_Event_Id_Enter = request.POST.get('Re_Event_Id_Enter')
        EventCoverPage = EventSection(Event_Cover_Title=Event_Cover_Title, Event_Id=Event_Id,
                                      Event_Cover_Page=Event_Cover_Page, Re_Enter_Id=Re_Event_Id_Enter)
        EventCoverPage.save()
        return HttpResponseRedirect('/EventImagesDashBoardHomePage')
    else:
        return HttpResponse("<h2>Method Now Allowed</h2>")


def EventPhotosPage(request):
    if request.method == 'POST':
        file = request.FILES["Upload_Image"]
        fs = FileSystemStorage()
        Re_Event_Id_Enter = request.POST.get('Re_Event_Id_Enter')
        Upload_Image = fs.save(file.name, file)
        Event_Id = EventCode.objects.get(Event_Id=request.POST.get('Event_Id'))
        EventImage = EventImages(Upload_Image=Upload_Image, Event_Id=Event_Id, Re_Enter_Id=Re_Event_Id_Enter)
        EventImage.save()
        return HttpResponseRedirect('/EventImagesDashBoardHomePage')
    else:
        return HttpResponse("<h2>Method Now Allowed</h2>")


def Eventcode(request):
    if request.method == 'POST':
        Event_Id = request.POST.get('Event_Code')
        eventcod = EventCode(Event_Id=Event_Id)
        eventcod.save()
        eventcod.clean()
        return HttpResponseRedirect('/EventImagesDashBoardHomePage')
    else:
        return HttpResponse("<h2>Method Now Allowed</h2>")


def Magazineupload(request):
    return render(request, 'AdminDashbord/AddMagazine.html')


def SaveMagazineData(request):
    if request.method == 'POST':
        file = request.FILES["Magazine_Cover_Page"]
        fs = FileSystemStorage()
        Magazine_Cover_Page = fs.save(file.name, file)
        Magazine_Cover_Title = request.POST.get('Magazine_Cover_Title')
        Magazine_Link = request.POST.get('Magazine_Link')
        MAgazine = MagazineUpload(Magazine_Cover_Page=Magazine_Cover_Page, Magazine_Cover_Title=Magazine_Cover_Title,
                                  Magazine_Link=Magazine_Link)
        MAgazine.save()
        return render(request, 'AdminDashbord/AddMagazine.html')


def BlogHomePage(request):
    return render(request, 'AdminDashbord/BlogDataFromAdmin.html')


def BlogHomePageDataSave(request):
    if request.method == 'POST':
        file = request.FILES["NewsImages"]
        fs = FileSystemStorage()
        NewsImages = fs.save(file.name, file)
        BlogId = request.POST.get('BlogId')
        NewsTitle = request.POST.get('NewsTitle')
        NewsBlogNews = request.POST.get('NewsBlogNews')
        NewsThumbnailTitleNews = request.POST.get('NewsThumbnailTitleNews')
        NewsDate = request.POST.get('NewsDate')
        BlogNews = NewsAndEventsBlog(BlogId=BlogId,NewsImages=NewsImages, NewsTitle=NewsTitle, NewsBlogNews=NewsBlogNews, NewsThumbnailTitleNews=NewsThumbnailTitleNews, NewsDate=NewsDate)
        BlogNews.save()
        return HttpResponseRedirect('/BlogHomePage')
    else:
        return HttpResponse("<h2>Method Now Allowed</h2>")
