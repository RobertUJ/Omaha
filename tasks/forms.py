from django.forms import ModelForm, TextInput
from django.forms.widgets import  DateInput,Textarea
from tasks.models import tasksModel


class addTaskForm(ModelForm):
    class Meta:
        model = tasksModel
        widgets = {
            'name':TextInput(attrs={'placeholder':'Nombre tarea*'}),
            'description':TextInput(attrs={'placeholder':'descripcion'}),
            'start_date':DateInput(attrs={'placeholder':'Fecha inicial'}),
            'due_date':DateInput(attrs={'placeholder':'Fecha final*'}),
         }
        fields = '__all__'

# def __unicode__(self):
#     return "%s" % self.project_name