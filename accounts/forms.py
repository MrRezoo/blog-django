from inspect import getmembers

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.template.defaultfilters import pprint


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'type': 'password'}))


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'enter own username'}))

    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))

    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'type': 'password'}))

    def clean_email(self):
        # var_dump(self.cleaned_data)
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already exists')
            # raise ValidationError('This email already exists')
        return email
