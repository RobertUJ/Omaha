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

        def __unicode__(self):
            return "%s" % self.project_name