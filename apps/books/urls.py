from django.conf.urls import url

from .views import BookListView, SearchBookView, UserPublicProfileView

urlpatterns = [
    url(r'^$', BookListView.as_view(), name="booklist"),
    url(r'^buscar/$', SearchBookView.as_view(), name="searchbook"),

    url(r'^libro/(?P<pk>\d+)/$', UserPublicProfileView.as_view(), name="detail"),

    #url(r'^dashboard/$', UserDashboard.as_view(),name='user-dashboard'),

    #url(r'^buscar/$','books.views.search', name="search"),
    #url(r'^temas/$','books.views.listatemas', name="themes"),
    #url(r'^libro/(?P<id_libro>\d+)/$','books.views.detalle_libro', name="detail"),
]
