from django.conf.urls import patterns, url
from projects.views import IndexView, addProject


urlpatterns = patterns(
    '',
    url(  r'^todo/$', IndexView.as_view(), name="IndexView"),

)