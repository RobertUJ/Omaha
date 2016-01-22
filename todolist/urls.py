from django.conf.urls import patterns, url
from todolist.views import TodoListView, SpecificTaskView, addTaskView


urlpatterns = [
    url(  r'^todolist/$', TodoListView.as_view(), name='TodoListView'),
    url(  r'^specifictask/$', SpecificTaskView.as_view(), name='SpecificTaskView'),
    url(  r'^addtask/$', addTaskView.as_view(), name='AddTaskView'),

]

# urlpatterns = patterns(
#     '',
#     url(  r'^todolist/$', TodoListView.as_view(), name='TodoListView'),
#     url(  r'^specifictask/$', SpecificTaskView.as_view(), name='SpecificTaskView'),
#     url(  r'^addtask/$', addTaskView.as_view(), name='AddTaskView'),
#
# )