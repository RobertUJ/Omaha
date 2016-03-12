# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from accounts.models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password','email')


class RegisterProfileForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'required':'True'})
    )
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'required':'True'})
    )
    email = forms.EmailField()

    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username


    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual registrado.')
        return email

    class Meta:
        model = UserProfile
        fields = ('photo',)


