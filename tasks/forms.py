from django.forms import ModelForm, TextInput
from django.forms.widgets import  DateInput,Textarea
from tasks.models import tasksModel


class addTaskForm(ModelForm):
    class Meta:
        model = tasksModel
        fields = [
            'name',
            'description',
            'due_date',
        ]
        widgets = {
            'name':TextInput(attrs={'placeholder':'Nombre tarea*'}),
            'description':TextInput(attrs={'placeholder':'descripcion'}),
            'due_date':DateInput(attrs={'placeholder':'Fecha final*','class': 'form-control hasDatePicker',"required":"True"}),
         }

# def __unicode__(self):
#     return "%s" % self.project_name