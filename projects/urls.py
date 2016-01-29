from django.conf.urls import patterns, url
from projects.views import IndexView, addProject, viewProject


urlpatterns = [
    url(  r'^index/$', IndexView.as_view(), name="IndexView"),
    url(  r'^addProject/$', addProject.as_view(), name="addProjectView"),
    url(  r'^viewProject/(?P<id>.*)/$', viewProject.as_view(), name="viewProjectView"),

]