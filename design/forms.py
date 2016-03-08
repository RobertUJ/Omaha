from django import forms
from django.forms import ModelForm, TextInput
from django.forms.widgets import DateInput, Textarea, FileInput

from design.models import DesignModelRequest, DesignModelResponse, DesignMailModel, CommentsModel


class DesignFormRequest(ModelForm):
    class Meta:
        model = DesignModelRequest
        fields = '__all__'
        widgets = {
            'user_assigner':TextInput(attrs={'placeholder':'Usuario peticion'}),
            'assignment':TextInput(attrs={'placeholder':'Peticion'}),
            'asked_date':DateInput(attrs={'placeholder':'Fecha peticion'}),
            'tentative_date':DateInput(attrs={'placeholder':'Fecha tentativa'}),
            'comment':Textarea(attrs={'placeholder':'Comentario'}),
        }
        labels = {
            'user_assigner': 'Usuario peticion ',
            'assignment': 'Peticion',
            'platform':' plataforma',
            'type':'tipo',
            'asked_date': 'Fecha peticion',
            'tentative_date': 'Fecha tentativa',
            'comment': 'comentario',
        }

class DesignFormResponse(forms.ModelForm):
    class Meta:
        model = DesignModelResponse
        fields = [
            'project',
            'designer_assigned',
            'user_assigner',
            'assignment',
            'files',
            'platform',
            'type',
            'comment',
        ]
        labels = {
            'project':'Proyecto',
            'designer_assigned':'Diseno',
            'user_assigner':'Usuario asignado',
            'assignment':'Respuesta',
            'files':'Archivo',
            'platform':'Plataforma',
            'type':'Tipo',
            'comment':'Comentario',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = '__all__'
        widgets = {
            'comment': Textarea(attrs={'placeholder': 'commentario*'}),
        }
        labels = {
            'comment': 'commentario',
            'designer_assigned': 'Diseno',
            'user_assigner': 'Usuario asignado',
        }

class ContactForm(ModelForm):
    class Meta:
        model = DesignMailModel
        fields = '__all__'
        widgets = {
            'subject':TextInput(attrs={'placeholder':'Tema*'}),
            'email':TextInput(attrs={'placeholder': 'Email*'}),
        }
        labels = {
            'subjec':'Peticion ',
            'email':'correo',
        }

