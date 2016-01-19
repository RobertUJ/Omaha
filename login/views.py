from django.shortcuts import render, render_to_response


# Create your views here.
from django.template import RequestContext

from login.forms import LoginForm


def login_view(request):
    form = LoginForm()
    ctx = {'form':form}
    return render_to_response('login.html',ctx,context_instance=RequestContext(request))
