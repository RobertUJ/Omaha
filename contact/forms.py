# coding=utf-8
from django.forms import ModelForm, TextInput, Textarea
from contact.models import ContactModel


class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        widgets = {
            'name':TextInput(attrs={'placeholder':'Nombre*'}),
            'email':TextInput(attrs={'placeholder':'Email*'}),
        }
        labels = {
            'name':'nombre ',
            'email':'correo',
            'comment':'comentario',
        }
