from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import views as auth_views

from .forms import SignUpForm, LoginForm

def signup(request):
    auth_logout(request)
    if request.method == 'POST':
        request.POST = request.POST.copy()
        request.POST.__setitem__('username', request.POST['email'])
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth_login(user=user, request=request)
                return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    auth_logout(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid() or True:
            email = request.POST['email']
            raw_password = request.POST['password']
            user = authenticate(username=email, password=raw_password)
            if user is not None:
                auth_login(user=user, request=request)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'users/registration/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return render(request, 'users/registration/logout.html')
