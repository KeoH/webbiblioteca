from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'webbiblio.views.home', name='home'),
    # url(r'^webbiblio/', include('webbiblio.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','core.views.home', name='home'),

    url(r'^libros/', include('books.urls', namespace='books')),
    url(r'^autores/', include('authors.urls', namespace='authors')),
    
    url(r'^users/', include('user_profile.urls', namespace='users')),

    url(r'^contacto/$','contacts.views.contacto', name='contact'), 
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
