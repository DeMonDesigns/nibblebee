from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import views as auth_views

from .forms import SignUpForm, LoginForm

def signup(request):
    auth_logout(request)
    if request.method == 'POST':
        # request.POST = request.POST.copy()
        # request.POST.__setitem__('username', request.POST['email'])
        print(list(request.POST.items()))
        signup_request = {
            # 'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
            'username': request.POST['su_email'],
            'first_name': request.POST['su_firstname'],
            'last_name': request.POST['su_lastname'],
            'email': request.POST['su_email'],
            'password1': request.POST['su_password'],
            'password2': request.POST['su_cpassword']
        }
        form = SignUpForm(signup_request)
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
        login_request = {
            # 'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
            'username': request.POST['si_username'],
            'password': request.POST['si_password'],
        }
        form = LoginForm(login_request)
        if form.is_valid() or True:
            email_or_username = login_request['username']
            raw_password = login_request['password']
            user = authenticate(username=email_or_username, password=raw_password)
            if user is not None:
                auth_login(user=user, request=request)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'signin.html', {'form': form})


def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')
