from django.shortcuts import render
from django.views.generic.base import View
from projects.forms import addProjectForm
from projects.models import MainProject


class IndexView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        project = MainProject.objects.all()
        data = {
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




