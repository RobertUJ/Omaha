from django.conf.urls import patterns, url
from tickets.views import TicketsIndexView,SolvedTicketsView, AddTicketView, SpecificTicketView

urlpatterns = [
    url(r'^tickets/$', TicketsIndexView.as_view(), name='TicketsView'),
    url(r'^solvedTickets/$', SolvedTicketsView.as_view(), name='solvedTicketsView'),
    #url(r'^ticket/(?P<id>.*)/$', SpecificTicketView.as_view(), name='SpecificTicketView'),
    url(r'^ticket/(?P<id>.*)/$', SpecificTicketView.as_view(), name='SpecificTicketView'),
    url(r'^addticket/$', AddTicketView.as_view(), name='AddTicketView'),
]