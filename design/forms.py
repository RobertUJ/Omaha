from django.db.models.fields.files import ImageField
from django.forms import ModelForm, TextInput
from django.forms.widgets import EmailInput, NumberInput, URLInput, DateInput, Textarea, FileInput

from design.models import DesignModelRequest, DesignModelResponse


class DesignFormRequest(ModelForm):
    class Meta:
        model = DesignModelRequest
        widgets = {
            'user_assigner':TextInput(attrs={'placeholder':'Usuario peticion'}),
<<<<<<< HEAD
            'assignment':TextInput(attrs={'placeholder':'Tarea'}),
=======
            'assignment':Textarea(attrs={'placeholder':'Tarea'}),
>>>>>>> 6b3039ac91be53dd5ddfc7ca3e4598c0bb016f0b
            'platform':TextInput(attrs={'placeholder':'Plataforma'}),
            'type':TextInput(attrs={'placeholder':'Tipo'}),
            'asked_date':DateInput(attrs={'placeholder':'Fecha peticion'}),
            'tentative_date':DateInput(attrs={'placeholder':'Fecha tentativa'}),
            'comment':Textarea(attrs={'placeholder':'Comentario'}),
        }
        fields = '__all__'

class DesignFormResponse(ModelForm):
    class Meta:
        model = DesignModelResponse
        widgets = {
            'designer_assigned':TextInput(attrs={'placeholder':'Disenador asignado'}),
            'user_assigned':Textarea(attrs={'placeholder':'Usuario peticion'}),
            'assignment':TextInput(attrs={'placeholder':'peticion'}),
            'files':FileInput(),
            'platform':DateInput(attrs={'placeholder':'Fecha peticion'}),
            'type':DateInput(attrs={'placeholder':'Fecha tentativa'}),
            'comment':Textarea(attrs={'placeholder':'Comentario'}),
        }
        fields = '__all__'
