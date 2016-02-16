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
        pdfDocumentos = documentsModel.objects.filter(type=1)
        imgDocumentos = documentsModel.objects.filter(type=3)
        imgDisenos = DesignModelResponse.objects.all
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
    def post(self, request, *args, **kwargs):
            form = DocumentForm(request.POST)
            data = {
                'form': form,
            }
            if form.is_valid():
                form.save(commit=True)
                return render(request, self.template_name,data)
            else:
                return render(request,self.template_name,data)
# class UploadDocumentView(View):
#     template_name = "uploadDocument.html"
#
#     def get(self, request, *args, **kwargs):
#         form = DocumentForm()
#         data = {
#             'form':form,
#         }
#         return render(request,self.template_name,data)
#
#     def post(self, request, *args, **kwargs):
#             form = DocumentForm(request.POST or None, request.FILES or None)
#             data = {
#                 'form': form,
#             }
#             if form.is_valid():
#                 form.save(commit=True)
#                 return render(request,self.template_name,data)
#             else:
#                 return render(request,self.template_name,data)
#             if form.is_valid():
#                 form.save(commit=True)
