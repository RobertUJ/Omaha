from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from projects.models import MainProject
from tasks.models import tasksModel
from todolist.models import todolistmodel
from todolist.forms import addTodoListForm


class TodoListView(View):
    template_name = "todolist.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs): 
        todo = todolistmodel.objects.all()
        data = {
            'todo': todo,
        }

        return render(request, self.template_name, data)


class SpecificTodoListView(View):
    template_name = "specifictodo.html"

    def get(self, request, *args, **kwargs):
        # project = get_object_or_404(MainProject, name=kwargs['name'])
        todolist = get_object_or_404(todolistmodel, pk=kwargs['id'])
        specifictask = tasksModel.objects.filter(todolist=todolist) 
        data = {
            # 'project': project,
            'todolist': todolist,
            'specifictask': specifictask,
        }

        return render(request, self.template_name, data)


class AddTodoListView(View):
    template_name = "addtodolist.html"

    def get(self, request, *args, **kwargs):
        form = addTodoListForm()
        projects = MainProject.objects.all()
        data = {
            'form': form,
            'projects': projects,
        }
        return render(request,self.template_name,data)

    def post(self,request,*args,**kwargs):
            form = addTodoListForm(request.POST)
            data = {
                'form': form,
            }
            if form.is_valid():
                form.save(commit=True)
                message = 'Lista agregada con exito'
                data['message']=message
                return render(request,self.template_name,data)
            else:
                return render(request,self.template_name,data)