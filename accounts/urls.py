# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registro/$',views.RegisterView.as_view(), name='accounts.register'),
<<<<<<< HEAD
    url(r'^perfil/$',views.ProfileView.as_view(),name='user.profile'),
    url(r'^editar_perfil/$',views.EditProfileView.as_view(),name='edit.account')
=======
    url(r'^perfil/$',views.ProfileView.as_view(),name='user.account'),
>>>>>>> 6a89ede279fa25ca4913de701889e8b6ccc29ab5
]