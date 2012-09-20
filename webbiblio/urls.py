from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webbiblio.views.home', name='home'),
    # url(r'^webbiblio/', include('webbiblio.foo.urls')),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','webbiblio.views.home'),
    url(r'^listalibros/$','webbiblio.views.listalibros'),
    url(r'^libro/(?P<id_libro>\d+)/$','webbiblio.views.detalle_libro'),
    url(r'^listaautores/$','webbiblio.views.listaautores'),
    url(r'^contacto/$','formularios.views.contacto'),
    url(r'^autor/(?P<id_autor>\d+)/$','webbiblio.views.detalle_autor'), 
)
