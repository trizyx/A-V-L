from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Log in',widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.TextInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-input'}),
            'password1' : forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2' : forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Log in',widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    email = forms.EmailField(label='email')
    def form_valid(self, form):
        print(form.cleaned_data)



