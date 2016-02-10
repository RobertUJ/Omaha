
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic.base import View
from design.models import DesignModelResponse
from design.forms import DesignFormRequest, DesignFormResponse

class DesignView(View):
    template_name = "design.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        designs = DesignModelResponse.objects.all()
        data = {
            'designs': designs,
        }
        return render(request, self.template_name, data)

class DesignRequestView(View):
    template_name = "designrequest.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        form = DesignFormRequest()
        data = {
            'form':form,
        }
        return render(request,self.template_name,data)

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def post(self,request,*args,**kwargs):
            form = DesignFormRequest(request.POST)
            data = {
                'form': form,
            }
            if form.is_valid():
                form.save(commit=True)
                return render(request,self.template_name,data)
            else:
                return render(request,self.template_name,data)

class DesignResponseView(View):
    template_name = "designresponse.html"
    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        form = DesignFormResponse()
        data = {
            'form':form,
        }
        return render(request,self.template_name,data)

    def post(self,request,*args,**kwargs):
            form = DesignFormResponse(request.POST or None, request.FILES or None)
            data = {
                'form': form,
            }
            if form.is_valid():
                form.save(commit=True)
                return render(request,self.template_name,data)
            else:
                return render(request,self.template_name,data)