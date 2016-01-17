from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(witget=forms.TextInput())
    password = forms.CharField(witget=forms.PasswordInput())

