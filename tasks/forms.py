from django.forms import ModelForm, TextInput
from django.forms.widgets import  DateInput,Textarea
from tasks.models import tasksModel


class addTaskForm(ModelForm):
    class Meta:
        model = tasksModel
        widgets = {
            'name':TextInput(attrs={'placeholder':'Nombre tarea*'}),
            'description':Textarea(attrs={'placeholder':'descripcion'}),
            'start_date':DateInput(attrs={'placeholder':'Fecha inicial'}),
            'due_date':DateInput(attrs={'placeholder':'Fecha final*'}),
         }
        fields = '__all__'
        labels = {
            'project':'Proyecto',
            'todolist':'Lista',
            'name':'Nombre',
            'description':'Descripcion',
            'start_date':'Fecha de inicio',
            'due_date':'Fecha de entrega',
            'user_assigned':'Usuario peticion',
            'user_assigner':'Usuario asignado',
        }

# def __unicode__(self):
#     return "%s" % self.project_name