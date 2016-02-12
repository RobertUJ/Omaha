from django.conf.urls import patterns, url
from design.views import DesignView, DesignRequestView, DesignResponseView, SpecificDesignView

urlpatterns = [
    url(r'^design/$', DesignView.as_view(), name="DesignView"),
    url(r'^diseno.(?P<id>.*)/$', SpecificDesignView.as_view(), name="SpecificDesignView"),
    url(r'^designrequest/$', DesignRequestView.as_view(), name="DesignRequestView"),
    url(r'^designresponse/$', DesignResponseView.as_view(), name="DesignResponseView"),
]