
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.utils.decorators import method_decorator

from login.forms import LoginForm

from django.views.generic import TemplateView, FormView



class LoginView(FormView):
    template_name = "login.html"
    #form = LoginForm
    mensaje = ""

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/index')
        else:
            form = LoginForm()
            ctx = {'form':form}
            if request.session.get("login"):
                return render('inicio_de_sesion')
            return  render(request,self.template_name,ctx)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return  HttpResponseRedirect('/index')
        else:
            mensaje = ""
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/index')
                        print "Te has identificado de modo correcto"
                    else:
                        mensaje = "Tu usuario esta inactivo"
                else:
                    mensaje = "Nombre y/o password incorrectos"

            ctx = {'form':form,'mensaje':mensaje}
            return render(request,self.template_name,ctx)


class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Te has descnectado con exito.')
        return HttpResponseRedirect('/inicio_de_sesion')