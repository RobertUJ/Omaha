from django.contrib import admin

from tickets.models import ticketsModelResponse
from .models import ticketsModel

admin.site.register(ticketsModel)
admin.site.register(ticketsModelResponse)
