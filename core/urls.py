from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'webbiblio.views.home', name='home'),
    # url(r'^webbiblio/', include('webbiblio.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','core.views.home', name='home'),

    url(r'^libros/', include('books.urls', namespace='books')),
    url(r'^autores/', include('authors.urls', namespace='authors')),

    url(r'^contacto/$','contacts.views.contacto', name='contact'), 
)
