from django.conf.urls import patterns, include, url

from .views import Log_In, Log_Out

urlpatterns = patterns('',
    url(r'^login/$',Log_In.as_view(), name="login"),
    url(r'^logout/$',Log_Out.as_view(), name="logout"),
)
