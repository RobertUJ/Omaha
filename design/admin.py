from django.contrib import admin

from design.models import CommentsModel
from .models import DesignModelRequest, DesignModelResponse

admin.site.register(DesignModelRequest)
admin.site.register(DesignModelResponse)
admin.site.register(CommentsModel)
