from unicodedata import name

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from projects.models import MainProject
from tickets.forms import AddTicketForm
from tickets.models import ticketsModel


class TicketsIndexView(View):
    template_name = "tickets.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        tickets = ticketsModel.objects.all()
        projects = MainProject.objects.all()
        print projects
        data = {
            'tickets': tickets,
            'projects': projects,
        }
        return render(request, self.template_name, data)


class AddTicketView(View):
    template_name = "addTicket.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        form = AddTicketForm()
        data = {
            'form': form,
        }

        return render(request,  self.template_name,  data)

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def post(self,request,*args,**kwargs):
            form = AddTicketForm(request.POST)
            data = {
                'form': form,

            }
            if form.is_valid():
                form.save(commit=True)
                return render(request,self.template_name,data)
            else:
                return render(request,self.template_name,data)