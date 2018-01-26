from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    user = request.user
    message = "Your are not logged in."
    if not user.is_anonymous:
        message = "hello there!"
    return render(request, 'nibble_bee/index.html', {'user': user, 'message': message})


# @login_required(login_url="login/")
