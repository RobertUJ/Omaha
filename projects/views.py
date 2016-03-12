from unicodedata import category

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import response
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from design.models import DesignModelRequest, DesignModelResponse
from documents.models import documentsModel
from feeds.models import CommentModel, DiscussionModel
from projects.forms import addProjectForm, addCommentForm
from projects.models import MainProject
from tickets.models import ticketsModel
from todolist.models import todolistmodel


# -------------------------Menu principal(vista de proyectos)-----------------------

class IndexView(View):
    template_name = "index.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        project = MainProject.objects.order_by('due_date')
        data = {
            'project': project,
        }
        return render(request, self.template_name, data)


# --------------------Ver proyecto(detalles)-------------------------

class viewProject(View):
    template_name = "viewProject.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(MainProject, name=kwargs['name'])
        todolist = todolistmodel.objects.filter(project=project)
        tickets = ticketsModel.objects.filter(project=project)
        designRequests = DesignModelRequest.objects.filter(project=project)
        imgDocuments = documentsModel.objects.filter(project=project)
        imgDesign = DesignModelResponse.objects.filter(project=project)
        comments = CommentModel.objects.filter(discussion__category="projects")
        commentForm = addCommentForm()
        data = {
            'todolist': todolist,
            'tickets': tickets,
            'project': project,
            'designRequests': designRequests,
            'imgDesign': imgDesign,
            'imgDocuments': imgDocuments,
            'comments':comments,
            'commentsForm': commentForm,
        }
        return render(request, self.template_name, data)

    # ----------------------Agregar comentario-------------------------

    def post(self, request, *args, **kwargs):
        commentForm = addCommentForm(request.POST, request.FILES)
        ctx = {
            'commentsForm': commentForm
        }
        if commentForm.is_valid():
            title = commentForm.cleaned_data["title"]
            body = commentForm.cleaned_data["body"]
            project = get_object_or_404(MainProject, name=kwargs['name'])
            projectpk = project.pk
            try:
                discussion = DiscussionModel.objects.get(category="projects", id_category=projectpk)
            except Exception:
                discussion = None
            if not discussion:
                discussion = DiscussionModel.objects.create(id_category=projectpk, category="projects")
                discussion.save()
            CommentModel.objects.create(body=body, title=title, discussion=discussion, author=request.user)
            return redirect('/')
        return render(request, self.template_name,ctx)


# -----------------------Agregar proyecto---------------------

class addProject(View):
    template_name = "addProject.html"

    def get(self, request, *args, **kwargs):
        form = addProjectForm()
        data = {
            'form': form,
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        form = addProjectForm(request.POST)
        data = {
            'form': form,
        }
        if form.is_valid():
            name = form.cleaned_data["name"]
            # start_date = form.cleaned_data["start_date"]
            due_date = form.cleaned_data["due_date"]
            url = form.cleaned_data["url"]
            domain = form.cleaned_data["domain"]
            server = form.cleaned_data["server"]
            client = form.cleaned_data["client"]
            platform = form.cleaned_data["platform"]
            users = form.cleaned_data["users"]

            new_element = MainProject.objects.create(user=request.user, name=name, due_date=due_date, url=url,
                                                     domain=domain, server=server, client=client,
                                                     platform=platform, users=users)
            new_element.save()

            return HttpResponseRedirect('/index')
        else:
            return render(request, self.template_name, data)
