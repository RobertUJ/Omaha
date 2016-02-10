from django.conf.urls import patterns, url
from tasks.views import TasksIndexView, SpecificTaskView, AddTaskView


urlpatterns = [
    url(  r'^todolist/tasks/$', TasksIndexView.as_view(), name='TasksView'),
    url(  r'^todolist/specifictask/$', SpecificTaskView.as_view(), name='SpecificTaskView'),
    url(  r'^tareas.(?P<id>.*)/$', AddTaskView.as_view(), name='AddTaskView'),
]