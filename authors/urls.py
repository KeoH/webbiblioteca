from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$','authors.views.listaautores'),
    url(r'^autor/(?P<id_autor>\d+)/$','authors.views.detalle_autor'), 
)