from django.db.models.fields.files import ImageField
from django.forms import ModelForm, TextInput
from django.forms.widgets import EmailInput, NumberInput, URLInput, DateInput, Textarea, FileInput

from todolist.models import todolistmodel


class todolistform(ModelForm):
    class Meta:
        model = todolistmodel
        widgets = {
            'name':TextInput(attrs={'placeholder':'Nombre tarea*', 'class':"inputs_proyect"}),
            'task':Textarea(attrs={'placeholder':'Tarea*'}),
            'start_date':DateInput(attrs={'placeholder':'Fecha inicial'}),
            'end_date':DateInput(attrs={'placeholder':'Fecha final*'}),
            'user_assigned':TextInput(attrs={'placeholder':'Usuario asignado*'}),
            'user_assigner':TextInput(attrs={'placeholder':' peticion*'}),
            'type':TextInput(attrs={'placeholder':'Tipo*'}),
            'client':TextInput(attrs={'placeholder':'Cliente*'}),
            'platform':TextInput(attrs={'placeholder':'Plataforma*'}),
            'priority':NumberInput(attrs={'placeholder':'Prioridad*'}),
            'users':TextInput(attrs={'placeholder':'usuarios*'})
        }
        fields = '__all__'

   # def __unicode__(self):
   #     return "%s" % self.project_name