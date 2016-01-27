# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, TextInput, DateInput, PasswordInput, EmailInput

from accounts.models import UserProfile


class RegisterForm(ModelForm):
    class Meta:
        model = UserProfile
        widgets = {
            'username':TextInput(attrs={'placeholder':'Usuario'}),
            'email':EmailInput(attrs={'placeholder':'Email'}),
            'password':PasswordInput(attrs={'placeholder':'Contraseña'}),
            'password2':PasswordInput(attrs={'placeholder':'Contraseña'}),
        }
        fields = '__all__'

        #username = forms.CharField(min_length=5)
        #email = forms.EmailField()
        #password = forms.CharField(min_length=5, widget=forms.PasswordInput())
        #password2 = forms.CharField(widget=forms.PasswordInput())
        #photo = forms.ImageField(required=False)
    # -*- coding: utf-8 -*-
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
                raise forms.ValidationError('Ya existe un email igual en la db.')
            return email

        def clean_password2(self):
            """Comprueba que password y password2 sean iguales."""
            password = self.cleaned_data['password']
            password2 = self.cleaned_data['password2']
            if password != password2:
                raise forms.ValidationError('Las contraseñas no coinciden.')
            return password2
