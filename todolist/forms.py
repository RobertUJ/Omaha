from django.forms import ModelForm, TextInput
from django.forms.widgets import EmailInput, NumberInput, URLInput, DateInput,Textarea
from todolist.models import todolistmodel


class addTaskForm(ModelForm):
    class Meta:
        model = todolistmodel
        widgets = {
            'name':TextInput(attrs={'placeholder':'Nombre tarea*'}),
            'description':Textarea(attrs={'placeholder':'descripcion'}),
            'start_date':DateInput(attrs={'placeholder':'Fecha inicial'}),
            'due_date':DateInput(attrs={'placeholder':'Fecha final*'}),
         }
        fields = '__all__'

# def __unicode__(self):
#     return "%s" % self.project_name