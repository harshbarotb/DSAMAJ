from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Create your views here.


def Home(request):
    news = NewsAndEventsBlog.objects.all()
    params = {'news': news}
    return render(request, 'HomePage/index.html', params)


def login(request):
    return render(request, 'HomePage/MEM_LOGIN.html')


def ShowBlog(request, i_BlogId):
    blog = NewsAndEventsBlog.objects.filter(BlogId=i_BlogId)
    return render(request, 'HomePage/BLOG.html', {'blog': blog})
