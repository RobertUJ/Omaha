from functools import partial

from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm, TextInput
from django.forms.widgets import EmailInput, NumberInput, URLInput, DateInput

from projects.models import MainProject
# DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class addProjectForm(ModelForm):
    class Meta:
        model = MainProject
        fields = [
            'name',
            'due_date',
            'url',
            'domain',
            'server',
            'client',
            'platform',
            'users',
        ]

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Nombre*', "required":"True"}),
            'due_date': DateInput(attrs={'placeholder':'Fecha final','class': 'form-control hasDatePicker'}),
            'url': TextInput(attrs={'placeholder': 'url*', "required":"True"}),
            'domain': TextInput(attrs={'placeholder':'dominio'}),
            'server': TextInput(attrs={'placeholder': 'servidor'}),
            'client': TextInput(attrs={'placeholder': 'cliente'}),
            'users': TextInput(attrs={'placeholder': 'usuarios'}),


        }




