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
                name = form.cleaned_data["name"]
                start_date = form.cleaned_data["start_date"]
                due_date = form.cleaned_data["due_date"]
                url = form.cleaned_data["url"]
                domain = form.cleaned_data["domain"]
                server = form.cleaned_data["server"]
                client = form.cleaned_data["client"]
                platform = form.cleaned_data["platform"]
                users = form.cleaned_data["users"]

                new_element = MainProject.objects.create(user=request.user,name=name,start_date=start_date,due_date=due_date,url=url,
                                                         domain=domain,server=server,client=client,
                                                         platform=platform,users=users)
                new_element.save()

                message = 'Agregado correctamente'
                data['message']=message
                return render(request, self.template_name, data)
            else:
                return render(request, self.template_name, data)




