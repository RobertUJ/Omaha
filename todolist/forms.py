from django.forms import ModelForm, TextInput
from django.forms.widgets import DateInput
from todolist.models import todolistmodel


class addTodoListForm(ModelForm):
    class Meta:
        model = todolistmodel
        widgets = {
            'name': TextInput(attrs={'placeholder':'Nombre lista*'}),
            'description': TextInput(attrs={'placeholder':'descripcion*'}),
            'start_date': DateInput(attrs={'placeholder':'Fecha inicial*'}),
            'due_date': DateInput(attrs={'placeholder':'Fecha final*'}),
        }
        fields = '__all__'

        labels = {
             'project':'proyecto',
             'name':'nombre',
             'description':'descripcion',
             'start_date':'nombre',
             'due_date':'Fecha de entrega',
        }

    def __unicode__(self):
        return "%s" % self.project_name


