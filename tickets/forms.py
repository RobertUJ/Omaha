from django.forms import ModelForm, TextInput, Select
from tickets.models import ticketsModel


class AddTicketForm(ModelForm):
    class Meta:
        model = ticketsModel
        widgets = {
            'description':TextInput(attrs={'placeholder':'descripcion'}),
            'user_reporter':TextInput(attrs={'placeholder':'Usuario peticion*'}),
            'user_assigned':TextInput(attrs={'placeholder':'Usuario asignado*'}),
         }
        fields = '__all__'

def __unicode__(self):
    return "%s" % self.project_name