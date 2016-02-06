from django.conf.urls import patterns, url

from modules.views import ModulesView, addModuleView


urlpatterns = [
    url(  r'^modulos/$', ModulesView.as_view(), name="ModulesView"),
    url(  r'^agregar_modulo/$', addModuleView.as_view(), name="addModuleView"),


]