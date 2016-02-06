from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from projects.forms import addProjectForm
from projects.models import MainProject
from todolist.models import todolistmodel


class IndexView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        # project = MainProject.objects.all()
        project = MainProject.objects.order_by('priority')
        data = {
            'project': project,
        } 
        return render(request, self.template_name, data)

class viewProject(View):
    template_name = "viewProject.html"

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(MainProject, pk=kwargs['id'])
        todolist = todolistmodel.objects.all()
        print  todolist
        data = {
             'todolist': todolist,
             'project': project,
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
                return render(request,self.template_name,data)
            else:
                # print form.e
                return render(request,self.template_name,data)




