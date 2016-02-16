# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registro/$',views.RegisterView.as_view(), name='accounts.register'),
    url(r'^perfil/$',views.ProfileView.as_view(),name='user.account'),
]