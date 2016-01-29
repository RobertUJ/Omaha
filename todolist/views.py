from django.shortcuts import render
from django.views.generic.base import View

from projects.models import MainProject
from todolist.models import todolistmodel
from todolist.forms import addTaskForm

class TodoListView(View):
    template_name = "todolist.html"

    def get(self, request, *args, **kwargs):
        tasks = todolistmodel.objects.all()
        data = {
            'tasks': tasks,
        }
        return render(request, self.template_name, data)

class SpecificTaskView(View):
    template_name = "specifictask.html"

    def get(self, request, *args, **kwargs):
        specifictask = todolistmodel.objects.all()
        data = {
            'specifictask': specifictask,
        }
        return render(request, self.template_name, data)

class addTaskView(View):
    template_name = "addtask.html"
    def get(self, request, *args, **kwargs):
        form = addTaskForm()
        projects = MainProject.objects.all()
        data = {
            'form':form,
            'projects': projects,
        }
        return render(request,self.template_name,data)

    def post(self,request,*args,**kwargs):
            form = addTaskForm(request.POST)
            data = {
                'form': form,

            }
            if form.is_valid():
                form.save(commit=True)
                return render(request,self.template_name,data)
            else:
                return render(request,self.template_name,data)
