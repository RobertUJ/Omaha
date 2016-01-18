
from django.conf.urls   import patterns, url

urlpatterns = patterns('omaha.users.views',
                       url(r'^$','login_view',name='inicio_sesion'),

)