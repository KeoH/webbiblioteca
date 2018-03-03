from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import home
from contacts.views import contacto

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^libros/', include('books.urls')),
    url(r'^contacto/$', contacto, name='contact'),
    url(r'^$', home, name='home')
]
