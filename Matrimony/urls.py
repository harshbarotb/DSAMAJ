from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexMatrimony, name='IndexMatrimony'),
    path('LoginUser/', views.LoginUser, name='LoginUser'),
    path('RegUser/', views.RegUser, name='RegUser'),
    path('SignUp/', views.SignUp, name='SignUp')
]
