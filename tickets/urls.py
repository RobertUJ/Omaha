from django.conf.urls import patterns, url
from tickets.views import TicketsIndexView, AddTicketView

urlpatterns = [
    url(r'^tickets/$', TicketsIndexView.as_view(), name='TicketsView'),
    url(r'^addticket/$', AddTicketView.as_view(), name='AddTicketView'),
]