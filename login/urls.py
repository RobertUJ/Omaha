from django.conf.urls import patterns, url

urlpatterns = patterns('login.views',
                       url(r'^$','login_view',name='inicio de sesion'),
                       )