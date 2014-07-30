from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$','books.views.listalibros'),
    url(r'^libro/(?P<id_libro>\d+)/$','books.views.detalle_libro'), 
)
