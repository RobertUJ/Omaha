from django.shortcuts import render
from django.views.generic import FormView
from accounts.forms import RegisterForm


class RegisterView(FormView):
    template_name = "register.html"


    def get(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        ctx = {
            'form': form
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST, request.FILES)
        ctx = {
             'form': form,
        }
        if form.is_valid():
            form.save()
            return render(request,self.template_name,ctx)
        else:
            # print form.e
            return render(request,self.template_name,ctx)