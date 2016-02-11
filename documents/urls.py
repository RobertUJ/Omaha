from django.conf.urls import patterns, url
from documents.views import DocumentsView, UploadDocumentView


urlpatterns = [
    url(r'^documents/$', DocumentsView.as_view(), name="DocumentsView"),
    url(r'^uploadDocument/$', UploadDocumentView.as_view(), name="UploadDocumentsView"),

]