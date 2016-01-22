from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic.base import View
from todolist.models import todolistmodel
from todolist.forms import todolistform

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
        form = todolistform()
        data = {
            'form':form,
        }
        return render(request,self.template_name,data)

    def post(self,request,*args,**kwargs):
            form = todolistform(request.POST)
            data = {
                'form': form,
            }
            if form.is_valid():
                form.save(commit=True)
                return render(request,self.template_name,data)
            else:
                return render(request,self.template_name,data)
=======

# Create your views here.
>>>>>>> 84bb6d606d47a31bfc3d0127ab829f743e58f464
