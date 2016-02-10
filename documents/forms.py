# coding=utf-8
from django.forms import ModelForm, TextInput, Textarea
from contact.models import ContactModel
from documents.models import documentsModel


class ContactForm(ModelForm):
    class Meta:
        model = documentsModel
        fields = '__all__'
        widgets = {
            'name':TextInput(attrs={'placeholder':'Nombre*'}),
        }
        labels = {
            'name':'nombre ', 
        }
