from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def user_login(request):
    return HttpResponse('Login form')
