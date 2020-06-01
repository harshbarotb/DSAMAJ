from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def IndexMatrimony(request):
    return render(request, 'Matrimony/MatrimonyIndex.html')


def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('MatrimonyIndex.html')
    context = {}
    return render(request, 'Matrimony/LogIn.html', context)


def RegUser(request):
    form = MatrimonyUserRegform()
    if request.method == 'POST':
        form = MatrimonyUserRegform(request.POST)
        FORM = UserCreationForm(request.POST)
        if form.is_valid():
            if FORM.is_valid():
                FORM.save()
                form.save()
                user = form.cleaned_data.get('First_Name')
                messages.success(request, 'Account Created for' + user)
                return redirect('/RegUser/')
    context = {'form': form}
    return render(request, 'Matrimony/Register.html', context)


def SignUp(request):
    FORM = UserCreationForm()
    if request.method == 'POST':
        FORM = UserCreationForm(request.POST)
        if FORM.is_valid():
            FORM.save()
            user = FORM.cleaned_data.get('username')
            messages.success(request, 'Account Created for' + user)
            return redirect('/RegUser/')
    context = {'forms': FORM}
    return render(request, 'Matrimony/Register.html', context)
