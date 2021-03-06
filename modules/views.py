from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from modules.forms import addModuleForm
from modules.models import Module


class ModulesView(View):
    template_name = "modules.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion'))
    def get(self, request, *args, **kwargs):
        form = addModuleForm()
        module = Module.objects.all()
        data = {
            'module': module,
            'form':form,
        }
        return render(request, self.template_name, data)

class addModuleView(View):
    template_name = "addModule.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion'))
    def get(self, request, *args, **kwargs):
        form = addModuleForm()
        data = {
            'form':form,
        }
        return render(request,self.template_name,data)

    @method_decorator(login_required(login_url='/inicio_de_sesion'))
    def post(self,request,*args,**kwargs):
            form = addModuleForm(request.POST)
            message = ''
            data = {
                'form': form,
            }
            if form.is_valid():
                form.save(commit=True)
                message = 'Se agrego correctamente'
                data['message']=message
                return render(request,self.template_name,data)
            else:
                # print form.e
                return render(request,self.template_name,data)


