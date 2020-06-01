from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserReg, name='UserReg')

]
