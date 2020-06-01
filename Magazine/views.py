from django.shortcuts import render
from .models import *


# Create your views here.


def Magazine(request):
    Magazine = MagazineUpload.objects.all()
    params = {'Magazine': Magazine}
    return render(request, 'Magazine/magazine.html', params)


def EventCoverPage(request):
    CoverPage = EventSection.objects.all()
    params = {'CoverPage': CoverPage}
    return render(request, 'Magazine/ImageSection.html', params)


def EventImagePage(request, i_Re_Enter_Id):
    Images = EventImages.objects.filter(Re_Enter_Id=i_Re_Enter_Id)
    params = {'Images': Images}
    return render(request, 'Magazine/ImagesOfImageSection.html', params)
