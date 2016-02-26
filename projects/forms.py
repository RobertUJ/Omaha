from functools import partial

from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm, TextInput
from django.forms.widgets import EmailInput, NumberInput, URLInput, DateInput

from projects.models import MainProject
# DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class addProjectForm(ModelForm):
    class Meta:
        model = MainProject
        name = forms.CharField(label='nombre')
        # start_date = forms.DateField(widget=AdminDateWidget)
        end_date = forms.DateField()
        url = forms.URLField()
        domain = forms.IPAddressField()
        server_assigned = forms.CharField()
        type = forms.CharField()
        client = forms.CharField()
        users = forms.CharField()

        fields = '__all__'

