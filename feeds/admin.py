from django.contrib import admin

# Register your models here.
from feeds.models import DiscussionModel, CommentModel

admin.site.register(DiscussionModel)
admin.site.register(CommentModel)

