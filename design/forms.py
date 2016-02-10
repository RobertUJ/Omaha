from django import forms
from django.db.models.fields.files import ImageField
from django.forms import ModelForm, TextInput
from django.forms.widgets import DateInput, Textarea, FileInput

from design.models import DesignModelRequest, DesignModelResponse


class DesignFormRequest(ModelForm):
    class Meta:
        model = DesignModelRequest
        widgets = {
            'user_assigner':TextInput(attrs={'placeholder':'Usuario peticion'}),
            'assignment':TextInput(attrs={'placeholder':'Tarea'}),
            'assignment':Textarea(attrs={'placeholder':'Tarea'}),
            'platform':TextInput(attrs={'placeholder':'Plataforma'}),
            'type':TextInput(attrs={'placeholder':'Tipo'}),
            'asked_date':DateInput(attrs={'placeholder':'Fecha peticion'}),
            'tentative_date':DateInput(attrs={'placeholder':'Fecha tentativa'}),
            'comment':Textarea(attrs={'placeholder':'Comentario'}),
        }
        fields = '__all__'

class DesignFormResponse(forms.ModelForm):
    class Meta:
        model = DesignModelResponse
        fields = [
            'designer_assigned',
            'user_assigner',
            'assignment',
            'files',
            'platform',
            'type',
            'comment',
        ]
        # fields = '__all__'

# class DesignFormResponse(ModelForm):
#     class Meta:
#         model = DesignModelResponse
#         widgets = {
#             'designer_assigned':TextInput(attrs={'placeholder':'Disenador asignado'}),
#             'user_assigner':TextInput(attrs={'placeholder':'Usuario peticion'}),
#             'assignment':TextInput(attrs={'placeholder':'peticion'}),
#             'files':ImageField(),
#             'platform':TextInput(attrs={'placeholder':'Fecha peticion'}),
#             'type':TextInput(attrs={'placeholder':'Fecha tentativa'}),
#             'comment':Textarea(attrs={'placeholder':'Comentario'}),
#         }
#         fields = '__all__'