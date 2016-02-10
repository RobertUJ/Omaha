from django.forms import ModelForm, TextInput
from django.forms.widgets import EmailInput, NumberInput, URLInput, DateInput

from projects.models import MainProject


class addProjectForm(ModelForm):
    class Meta:
        model = MainProject
        widgets = {
            'name':TextInput(attrs={'placeholder':'Nombre proyecto*', 'class':"inputs_proyect"}),
            'start_date':DateInput(attrs={'placeholder':'Fecha inicial'}),
            'end_date':DateInput(attrs={'placeholder':'Fecha final*'}),
            'url':URLInput(attrs={'placeholder':'URL*'}),
            'domain':TextInput(attrs={'placeholder':'Dominio*'}),
            'server_assigned':TextInput(attrs={'placeholder':'Servidor asignado*'}),
            'type':TextInput(attrs={'placeholder':'Tipo*'}),
            'client':TextInput(attrs={'placeholder':'Cliente*'}),
            'users':TextInput(attrs={'placeholder':'usuarios*'})
        }
        fields = '__all__'

   # def __unicode__(self):
   #     return "%s" % self.project_name