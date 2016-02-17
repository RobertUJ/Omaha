from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from design.models import DesignModelRequest, DesignModelResponse
from documents.models import documentsModel
from projects.forms import addProjectForm
from projects.models import MainProject
from tickets.models import ticketsModel
from todolist.models import todolistmodel


class IndexView(View):
    template_name = "index.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        #project = MainProject.objects.all()
        print "-"*50
        #print project
        project = MainProject.objects.order_by('due_date')

        data = {
            'project': project,
        } 
        return render(request, self.template_name, data)


class viewProject(View):
    template_name = "viewProject.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        # project = get_object_or_404(MainProject, name=kwargs['name'])
        project = get_object_or_404(MainProject, name=kwargs['name'])
        todolist = todolistmodel.objects.filter(project=project)
        tickets = ticketsModel.objects.filter(project=project)
        designRequests = DesignModelRequest.objects.filter(project=project)
        imgDocuments = documentsModel.objects.filter(project=project)
        imgDesign = DesignModelResponse.objects.filter(project=project)

        data = {
             'todolist': todolist,
             'tickets': tickets,
             'project': project,
             'designRequests': designRequests,
             'imgDesign': imgDesign,
             'imgDocuments': imgDocuments,
        }
        return render(request, self.template_name, data)


class addProject(View):
    template_name = "addProject.html"

    def get(self, request, *args, **kwargs):
        form = addProjectForm()
        data = {
            'form':form,
        }
        return render(request,self.template_name,data)

    def post(self,request,*args,**kwargs):
            form = addProjectForm(request.POST)
            data = {
                'form': form,
            }
            if form.is_valid():
                form.save(commit=True)
                return render(request, self.template_name, data)
            else:
                return render(request, self.template_name, data)




