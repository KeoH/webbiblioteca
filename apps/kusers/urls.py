from django.conf.urls import url
from .views import (
    UserPublicProfileView, UserPublicProfileListView,
    UserDashboard, UserLogin, UserLogout
    )

urlpatterns = [
    url(r'^$', UserPublicProfileListView.as_view(), name='public_profile-list'),
    url(r'^dashboard/$', UserDashboard.as_view(),name='user-dashboard'),

    url(r'^login/$', UserLogin.as_view(), name='login'),
    url(r'^logout/$', UserLogout.as_view(), name='logout'),

    url(r'^u/(?P<pk>[-\w]+)/$', UserPublicProfileView.as_view(), name='public-profile'),
]
