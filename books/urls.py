from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$','books.views.listalibros', name="home"),
    url(r'^buscar/$','books.views.search', name="search"),
    url(r'^temas/$','books.views.listatemas', name="themes"),
    url(r'^libro/(?P<id_libro>\d+)/$','books.views.detalle_libro', name="detail"), 
)
