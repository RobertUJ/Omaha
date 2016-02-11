from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from design.models import DesignModelResponse,DesignModelRequest
from design.forms import DesignFormRequest, DesignFormResponse
from projects.models import MainProject


class SpecificDesignView(View):
    template_name = "specificdesign.html"

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(MainProject, pk=kwargs['id'])
        designs = get_object_or_404(DesignModelRequest, pk=kwargs['id'])
        specificdesign = DesignModelRequest.objects.filter(project__designmodelrequest__comment__exact='Comentario1')
        print specificdesign
        data = {
            'project': project,
            'designs': designs,
            'specificdesign': specificdesign,
        }
        return render(request, self.template_name, data)

class DesignView(View):
    template_name = "design.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        designs = DesignModelRequest.objects.all()
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
            form = DesignFormRequest(request.POST)
            if form.is_valid():
                form.save(commit=True)

            send_mail("Peticion diseno " + str(request.POST.get('user_assigner')),
                      "PETICION: " + str(request.POST.get('assignment')) +" PLATAFORMA: "  + str(request.POST.get('platform'))
                      + " TIPO: " + str(request.POST.get('type')) + " COMENTARIO: " + str(request.POST.get('comment')),
                      request.POST.get('user_assigner'), ['erickhp12@gmail.com'])
            data = {
                'form': form,
            }
            return render(request, self.template_name, data)


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