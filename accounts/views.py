import json

import var_dump
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import pprint

from .forms import UserLoginForm, UserRegistrationForm


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('blog_app:all_articles')
            else:
                messages.error(request, 'wrong username or password', 'warning')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(data['username'], data['email'], data['password'])
            messages.success(request, 'you registered successfully, please login', 'success')
            return redirect('accounts:user_login')

    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'you logout successfully', 'success')
    return redirect('blog_app:all_articles')
