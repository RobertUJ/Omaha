from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template import RequestContext

from login.forms import LoginForm

from django.views.generic import TemplateView

from login.models import MainUsers


class LoginView(TemplateView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        ctx = {'form':form}
        if request.session.get("login"):
            return render('inicio_de_sesion')
        return  render(request,self.template_name,ctx)

    def post(self, request, *args, **kwargs):
        print request.POST
        mensaje = ""
        if request.method=="POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                print username
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        #return redirect(reverse('accounts.index'))
                        mensaje = "Te has identificado de modo correcto"
                    else:
                        mensaje = "Tu usuario esta inactivo"
                else:
                    mensaje = "Nombre y/o password incorrectos"

        form = LoginForm()
        ctx = {'form':form,'mensaje':mensaje}
        return render(request,self.template_name,ctx)

class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Te has descnectado con exito.')
        return render(reverse('inicio_de_sesion'))