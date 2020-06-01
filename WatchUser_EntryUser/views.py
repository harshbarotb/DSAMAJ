from django.shortcuts import render
from .models import *
from .filters import HeadPersonFilter
from UserEntry.models import *

# Create your views here.


def UserReg(request):
    headpersons = FamilyHead.objects.all()
    male = FamilyMember.objects.filter(M_Sex='Male')
    Female = FamilyMember.objects.filter(M_Sex='FeMale')
    FeMale_Count = Female.count()
    Count_Male = male.count()
    Count_Family = headpersons.count()
    myFilter = HeadPersonFilter(request.GET, queryset=headpersons)
    headpersons = myFilter.qs
    return render(request, 'WatchUser_EntryUser/userfinder.html', {'FeMale_Count': FeMale_Count, 'Count_Male': Count_Male, 'HeadPerson': headpersons, 'myFilter': myFilter, 'Count_Family': Count_Family})

