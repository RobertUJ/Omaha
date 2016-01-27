from django.conf.urls import patterns, url
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6b3039ac91be53dd5ddfc7ca3e4598c0bb016f0b
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
<<<<<<< HEAD
# )
=======
# )
=======
from projects.views import IndexView, addProject


urlpatterns = patterns(
    '',
    url(  r'^todo/$', IndexView.as_view(), name="IndexView"),

)
>>>>>>> 84bb6d606d47a31bfc3d0127ab829f743e58f464
>>>>>>> 6b3039ac91be53dd5ddfc7ca3e4598c0bb016f0b
