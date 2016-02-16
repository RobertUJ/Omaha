# coding=utf-8
from django.forms import ModelForm, TextInput, Textarea
from documents.models import documentsModel


class DocumentForm(ModelForm):
    class Meta:
        model = documentsModel
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Nombre*'}),
        }
        labels = {
            'project': 'Proyectos',
            'name': 'nombre ',
            'type': 'tipo ',
            'images': 'imagenes',
        }
