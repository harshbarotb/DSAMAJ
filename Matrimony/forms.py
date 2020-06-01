from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MatrimonyUserRegform(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = MatrimonyUserReg
        fields = ['First_Name', 'Last_Name', 'Cast', 'Email', 'HeadPerson', 'Degree', 'Study_Details', 'Password',
                  'DOB', 'Age', 'Father_PhoneNo', 'Height', 'Weight', 'Gender', 'Looking_For',
                  'Hobbies', 'Native_City', 'Current_City']


class UserCreationform(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']
