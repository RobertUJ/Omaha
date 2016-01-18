
from django.conf.urls.default   import patterns, url

urlpatterns = patterns('omaha.users.views',
                       url(r'^$','login_view',name='inicio_sesion'),

)