from django.conf.urls import patterns, url
from todolist.views import TodoListView, SpecificTodoListView, AddTodoListView


urlpatterns = [
    url(  r'^todolist/$', TodoListView.as_view(), name='TodoListView'),
    url(  r'^lista/(?P<id>.*)/$', SpecificTodoListView.as_view(), name='SpecificTodoListView'),
    url(  r'^addtodolist/$', AddTodoListView.as_view(), name='AddTodoListView'),

]

