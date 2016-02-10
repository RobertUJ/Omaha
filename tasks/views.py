from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from projects.models import MainProject
from tasks.models import todolistmodel
from tasks.forms import addTaskForm


class TasksIndexView(View):
    template_name = "tasks.html"

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


class AddTaskView(View):
    template_name = "addtask.html"

    def get(self, request, *args, **kwargs):
        proyectos = MainProject.objects.all()
        form = addTaskForm()
        todolist = get_object_or_404(todolistmodel, pk=kwargs['id'])
        # project = get_object_or_404(MainProject, name=kwargs['name'])

        data = {
            'form': form,
            'proyectos': proyectos,
            # 'project': project,
            'todolist': todolist,
        }

        return render(request,  self.template_name,  data)

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
