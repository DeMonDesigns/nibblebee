from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate as auth_authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import SignUpForm, LoginForm, EditProfileForm
from .backends import CustomAuthenticationBackend as user_auth

def signup(request):
    auth_logout(request)
    if request.method == 'POST':
        # request.POST = request.POST.copy()
        # request.POST.__setitem__('username', request.POST['email'])
        signup_request = {
            'username': request.POST['su_email'],
            'first_name': request.POST['su_firstname'],
            'last_name': request.POST['su_lastname'],
            'email': request.POST['su_email'],
            'password1': request.POST['su_password'],
            'password2': request.POST['su_cpassword']
        }
        if 'su_agree' in request.POST:
            signup_request['agree'] = request.POST['su_agree']
        form = SignUpForm(signup_request)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = user_auth().authenticate(username=username, password=raw_password)
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
            'userid': request.POST['si_username'],
            'password': request.POST['si_password'],
        }
        form = LoginForm(login_request)
        if form.is_valid():
            userid = login_request['userid']
            raw_password = login_request['password']
            user = user_auth().authenticate(username=userid, password=raw_password)
            if user is not None:
                auth_login(user=user, request=request)
                next_url = request.GET.get('next', None)
                if next_url is not None:
                    return redirect(next_url)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'signin.html', {'form': form})


def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')


@login_required(login_url='/users/login/?next=/users/profile/')
def view_profile(request, userid=''):
    requested_user = request.user
    if len(userid) != 0:
        try:
            requested_user = User.objects.get(username=userid)
        except User.DoesNotExist:
            return render(request, 'test-404.html')
    editable = False
    if request.user == requested_user:
        editable = True
    args = {
        'user': requested_user,
        'editable': editable,
    }
    return render(request, 'test-profile.html', args)


@login_required(login_url='/users/login/?next=/users/profile/')
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('/users/profile/')
    form = EditProfileForm(instance=user.userprofile)
    args = {
        'user': user,
        'form': form,
    }
    return render(request, 'test-edit-profile.html', args)

@login_required(login_url='/users/login/?next=/users/profile/')
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/users/profile/')
        else:
            return redirect('/users/settings/change-password')
    form = PasswordChangeForm(user=user)
    args = {
        'form': form,
        'user': user
    }
    return render(request, 'test-change-password.html', args)
