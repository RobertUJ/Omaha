from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from projects.forms import MainProject

def IndexView(request):
    form = MainProject()
    ctx = {'project_name': form}
    render_to_response('index.html', ctx, context_instance=RequestContext(request))

from projects.models import MainProject
class IndexView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        form = MainProject.objects.filter(project_name="Main project")
        data = {
            'project_name': form,
        }
        print form
        return render(request,self.template_name, data )
