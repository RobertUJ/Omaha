from django import forms

from login.models import MainUsers


class LoginForm(forms.Form):
    model = MainUsers
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))

