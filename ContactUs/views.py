from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def ContactUs(request):
    return render(request, 'ContactUs/contact.html')
