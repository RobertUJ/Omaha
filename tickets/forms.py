from django.forms import ModelForm, TextInput, Select
from tickets.models import ticketsModel


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
            'description':'Descripcion',
            'user_reporter':'Usuario peticion',
            'user_assigned':'Usuario asignado',
            'priority':'Prioridad',
        }
def __unicode__(self):
    return "%s" % self.project_name