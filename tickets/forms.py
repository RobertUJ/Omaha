from django.forms import ModelForm, TextInput, Select
from django.forms.widgets import Textarea

from tickets.models import ticketsModel,ticketsModelResponse


class AddTicketForm(ModelForm):
    class Meta:
        model = ticketsModel
        fields = '__all__'
        widgets = {
            'description':TextInput(attrs={'placeholder':'descripcion'}),
            'user_reporter':TextInput(attrs={'placeholder':'Usuario peticion*'}),
            'user_assigned':TextInput(attrs={'placeholder':'Usuario asignado*'}),
         }
        labels = {
            'project':'Proyecto',
            'description':'Descripcion',
            'user_reporter':'Usuario peticion',
            'user_assigned':'Usuario asignado',
            'priority':'Prioridad',
        }


def __unicode__(self):
    return "%s" % self.project_name


class AnswerTicketForm(ModelForm):
    class Meta:
        model = ticketsModelResponse
        fields = '__all__'
        widgets = {
            'response':Textarea(attrs={'placeholder':'descripcion'}),
         }
        labels = {
            'response':'Respuesta',
            'files':'Sube un archivo',
            # 'ticket_status':'Statuuus',
        }


def __unicode__(self):
    return "%s" % self.project_name