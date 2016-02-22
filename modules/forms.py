from django import forms
from django.forms import ModelForm, TextInput, DateInput, URLInput

from modules.models import Module


class addModuleForm(ModelForm):
    class Meta:
        model = Module

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Nombre Modulo*'}),
            'description': TextInput(attrs={'placeholder': 'Descripcion*'}),
            'justification': TextInput(attrs={'placeholder': 'Justificacion*'}),
            'analysis': TextInput(attrs={'placeholder': 'Analisis*'})
        }
        fields = '__all__'

        def clean_autor(self):
            modulo_limpio = self.cleaned_data
            name = modulo_limpio.get('name')
            if Module.objects.filter(name=name):
                raise forms.ValidationError("El autor debe contener mas de tres caracteres")
            return name


        def __unicode__(self):
            return "%s" % self.project_name