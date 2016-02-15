from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from design.models import DesignModelResponse
from documents.forms import DocumentForm
from documents.models import documentsModel


class DocumentsView(View):
    template_name = "documents.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        imgDocumentos = documentsModel.objects.all
        imgDisenos = DesignModelResponse.objects.all
        pdfDocumentos = documentsModel.objects.filter(type=1)
        data = {
            'imgDocumentos': imgDocumentos,
            'imgDisenos': imgDisenos,
            'pdfDocumentos': pdfDocumentos,
        }
        return render(request, self.template_name, data)


class UploadDocumentView(View):
    template_name = "uploadDocument.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def get(self, request, *args, **kwargs):
        form = DocumentForm()
        data = {
            'form':form,
        }
        return render(request,self.template_name,data)


    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def post(self,request,*args,**kwargs):
            form = DocumentForm(request.POST or None, request.FILES or None)
            data = {
                'form': form,
            }
            file_name = request.POST.get("files")

            if str(file_name).endswith('.pdf'):
                type = request.POST.get("type")
                documentsModel.type = type
                documentsModel.type = 1
            else:
                type = request.POST.get("type")
                documentsModel.type = type
                documentsModel.type = 5

            if form.is_valid():
                form.save(commit=True)
                return render(request,self.template_name,data)
            else:
                return render(request,self.template_name,data)

    @method_decorator(login_required(login_url='/inicio_de_sesion/'))
    def validate_file(self, file_name):
        if str(file_name).endswith('.pdf'):
            return 1
        if str(file_name).endswith('.docx'):
            return 2
        if str(file_name).endswith('.png'):
            return 3
        if str(file_name).endswith('.jpg'):
            return 4
        if str(file_name).endswith('.gif'):
            return 5
