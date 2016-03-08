from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from tickets.forms import AddTicketForm, AnswerTicketForm
from tickets.models import ticketsModel, ticketsModelResponse

from django.core.mail import send_mail

class TicketsIndexView(View):
    template_name = "tickets.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        ticketsPendientes = ticketsModel.objects.filter(status__iexact='1')
        ticketsSupersPendientes = []
        ticketsSupersResueltos = []

        for ticket in ticketsPendientes:
            ticketSuper = {}
            ticketSuper["id"] = ticket.id
            ticketSuper["description"] = ticket.description
            ticketSuper["user_assigned"] = ticket.user_assigned
            ticketSuper['project'] = ticket.project.all()
            ticketsSupersPendientes.append(ticketSuper)


        data = {
            'ticketsPendientes': ticketsSupersPendientes,
            'ticketsResueltos': ticketsSupersResueltos,
        }
        return render(request, self.template_name, data)


class SolvedTicketsView(View):
    template_name = "solvedTickets.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        tickets = ticketsModel.objects.filter(status__iexact='2')
        ticketsSupers = []

        for ticket in tickets:
            ticketSuper = {}
            ticketSuper["id"] = ticket.id
            ticketSuper["description"] = ticket.description
            ticketSuper["user_assigned"] = ticket.user_assigned
            ticketSuper['project'] = ticket.project.all()
            ticketsSupers.append(ticketSuper)

        data = {
            'tickets': ticketsSupers ,
        }
        return render(request, self.template_name, data)


class SpecificTicketView(View):
    template_name = "viewTickets.html"
    ticket_id = 1

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        tickets = get_object_or_404(ticketsModel, pk=kwargs['id'])
        ticket_answer = ticketsModelResponse.objects.all
        form = AnswerTicketForm()

        data = {
            'tickets': tickets,
            'ticket_answer': ticket_answer,
            'form': form,
        }
        return render(request,  self.template_name,  data)

    def post(self, request, *args, **kwargs):
            tickets = get_object_or_404(ticketsModel, pk=kwargs['id'])
            form = AnswerTicketForm(request.POST or None, request.FILES or None)
            data = {
                'form': form,
                'tickets': tickets,
            }
            if form.is_valid():
                form.save(commit=True)
                new_answerd = form.save(commit=True)
                new_answerd.ticket = tickets

                new_answerd.save()
                tickets.status = request.POST.get('status')
                tickets.save()
                return render(request, self.template_name, data)
            else:
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
            form = AddTicketForm(request.POST or None, request.FILES or None)
            data = {
                'form': form,
            }
            if form.is_valid():
                send_mail("Peticion ticket " + str(request.POST.get('user_reporter')),
                "PETICION: " + str(request.POST.get('description')),request.POST.get('user_assigner'), ['erickhp12@gmail.com'])

                form.save(commit=True)
                message = 'Se agrego correctamente el ticket'
                data['message']=message
                return render(request,self.template_name,data)
            else:
                return render(request,self.template_name,data)

