from django.conf.urls import url
from .views import LoginView, LogoutView

urlpatterns = [
    url(r'^inicio_de_sesion/', LoginView.as_view(), name='login.view.url'),
    url(r'^logout/', LogoutView.as_view(), name='logout.view.url'),
]