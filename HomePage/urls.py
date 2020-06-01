from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('ShowBlog/<str:i_BlogId>', views.ShowBlog, name='ShowBlog'),
]
