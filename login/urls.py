from django.conf.urls import url
from .views import LoginView

urlpatterns = [
    url(r'^inicio_de_sesion/', LoginView.as_view(), name='login.view.url'),
]