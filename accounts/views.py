from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserLoginForm


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})
