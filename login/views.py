from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import request
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template import RequestContext

from login.forms import LoginForm

from django.views.generic import TemplateView, FormView

from login.models import MainUsers


class LoginView(FormView):
    template_name = "login.html"
    #form = LoginForm
    mensaje = ""

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        ctx = {'form':form}
        if request.session.get("login"):
            return render('inicio_de_sesion')
        return  render(request,self.template_name,ctx)

    def form_valid(self, form):
        mensaje = ""
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        print username
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                print username
                #return redirect(reverse('index'))
                mensaje = "Te has identificado de modo correcto"
            else:
                mensaje = "Tu usuario esta inactivo"
                print mensaje
        else:
            mensaje = "Nombre y/o password incorrectos"
            print mensaje
        ctx = {'form':form,'mensaje':mensaje}
        return super(LoginView, self).form_valid(form)


    def post(self, request, *args, **kwargs):
        #print request.POST


        form = LoginForm(request.POST)
        ctx = {'form':form}
        return render(request,self.template_name,ctx)

class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Te has descnectado con exito.')
        return render(reverse('inicio_de_sesion'))