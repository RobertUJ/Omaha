# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from accounts.forms import RegistroUserForm


def registro_usuario_view(request):
    if request.method == 'POST':
        form = RegistroUserForm(request.POST, request.FILES)
    else:
        form = RegistroUserForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)