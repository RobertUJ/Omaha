from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template import RequestContext

from login.forms import LoginForm

from django.views.generic import TemplateView, FormView



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



    def post(self, request, *args, **kwargs):
        #print request.POST
        mensaje = ""
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print request.POST
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    #login(request,user)
                    #return redirect(reverse('projects:IndexView'))
                    mensaje = "Te has identificado de modo correcto"
                    print  mensaje
                else:
                    mensaje = "Tu usuario esta inactivo"
                    print  mensaje
            else:
                mensaje = "Nombre y/o password incorrectos"
                print  mensaje
        #else:
            #print "no, algo esta mal"

        ctx = {'form':form,'mensaje':mensaje}
        return render(request,self.template_name,ctx)


class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Te has descnectado con exito.')
        return render(reverse('inicio_de_sesion'))