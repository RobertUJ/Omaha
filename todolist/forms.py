<<<<<<< HEAD
from django.db.models.fields.files import ImageField
from django.forms import ModelForm, TextInput
from django.forms.widgets import EmailInput, NumberInput, URLInput, DateInput, Textarea, FileInput
=======
<<<<<<< HEAD
from django.db.models.fields.files import ImageField
from django.forms import ModelForm, TextInput
from django.forms.widgets import EmailInput, NumberInput, URLInput, DateInput, Textarea, FileInput
=======
from django.forms import ModelForm, TextInput
from django.forms.widgets import EmailInput, NumberInput, URLInput, DateInput
>>>>>>> 84bb6d606d47a31bfc3d0127ab829f743e58f464
>>>>>>> 6b3039ac91be53dd5ddfc7ca3e4598c0bb016f0b

from todolist.models import todolistmodel


<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6b3039ac91be53dd5ddfc7ca3e4598c0bb016f0b
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
<<<<<<< HEAD
=======
=======
class addProjectForm(ModelForm):
    class Meta:
        model = todolistmodel
        widgets = {
            'name':TextInput(attrs={'placeholder':'Nombre proyecto*', 'class':"inputs_proyect"}),
            'start_date':DateInput(attrs={'placeholder':'Fecha inicial'}),
            'end_date':DateInput(attrs={'placeholder':'Fecha final*'}),
            'url':URLInput(attrs={'placeholder':'URL*'}),
            'domain':TextInput(attrs={'placeholder':'Dominio*'}),
            'server_assigned':TextInput(attrs={'placeholder':'Servidor asignado*'}),
>>>>>>> 84bb6d606d47a31bfc3d0127ab829f743e58f464
>>>>>>> 6b3039ac91be53dd5ddfc7ca3e4598c0bb016f0b
            'type':TextInput(attrs={'placeholder':'Tipo*'}),
            'client':TextInput(attrs={'placeholder':'Cliente*'}),
            'platform':TextInput(attrs={'placeholder':'Plataforma*'}),
            'priority':NumberInput(attrs={'placeholder':'Prioridad*'}),
            'users':TextInput(attrs={'placeholder':'usuarios*'})
        }
        fields = '__all__'

   # def __unicode__(self):
   #     return "%s" % self.project_name