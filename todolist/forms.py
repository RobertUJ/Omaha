from django.forms import ModelForm, TextInput
from django.forms.widgets import DateInput,Textarea, Select
from todolist.models import todolistmodel

class addTodoListForm(ModelForm):
    class Meta:
        model = todolistmodel
        widgets = {
            'name': TextInput(attrs={'placeholder':'Nombre lista*'}),
            'description': Textarea(attrs={'placeholder':'descripcion'}),
            'due_date': DateInput(attrs={'placeholder':'Fecha final*'}),
         }
        fields = ['name','description','due_date',]


    def __unicode__(self):
     return "%s" % self.project_name


