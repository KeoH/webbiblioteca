from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','core.views.home', name='home'),

    url(r'^libros/', include('apps.books.urls', namespace='books')),
    #url(r'^autores/', include('apps.authors.urls', namespace='authors')),

    url(r'^users/', include('apps.kusers.urls', namespace='users')),

    url(r'^contacto/$','apps.contacts.views.contacto', name='contact'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
