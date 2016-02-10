from django.conf.urls import patterns, url
from documents.views import DocumentsView


urlpatterns = [
    url(r'^documents/$', DocumentsView.as_view(), name="DocumentsView"),

]