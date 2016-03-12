from django import forms
from django.forms import ModelForm, TextInput, Form
from django.forms.widgets import DateInput

from feeds.models import Comment
from projects.models import MainProject

class addProjectForm(forms.ModelForm):
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
            'due_date': DateInput(attrs={'placeholder':'Fecha final','class': 'form-control hasDatePicker',"required":"True"}),
            'url': TextInput(attrs={'placeholder': 'url*', "required":"True"}),
            'domain': TextInput(attrs={'placeholder':'dominio'}),
            'server': TextInput(attrs={'placeholder': 'servidor'}),
            'client': TextInput(attrs={'placeholder': 'cliente'}),
            'users': TextInput(attrs={'placeholder': 'usuarios'}),


        }

class addCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'title',
            'body',
        ]

        widgets = {
            'title': TextInput(attrs={"required":"True"}),
            'body': TextInput(attrs={'placeholder':'Comentario',"required":"True"}),
        }


