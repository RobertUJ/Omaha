from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import View

from contact.forms import ContactForm


class ContactView(View):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        data = {
            'form': form,
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=False)

        send_mail(request.POST.get('name') +" Omaha ", request.POST.get('comment'),request.POST.get('email'), ['erickhp12@gmail.com'])

        data = {
            'form': form,
            'app_name': settings.APP_NAME
        }
        return render(request, self.template_name, data)
