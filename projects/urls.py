from django.conf.urls import patterns, url
from projects.views import IndexView, addProject


urlpatterns = patterns(
    '',
    url(  r'^index/$', IndexView.as_view(), name="IndexView"),
    url(  r'^addProject/$', addProject.as_view(), name="addProjectView"),

)