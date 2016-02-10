from django.conf.urls import patterns, url
from contact.views import ContactView

urlpatterns = [
    url(  r'^contact/$', ContactView.as_view(), name="ContactView"),

]