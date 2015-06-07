from django.conf.urls import url
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    # /artworks/
    # /artworks/page/2/
    url(r'^$', 'artworks.views.artwork_list', name='artwork_list'),
    url(r'^page/1/$', RedirectView.as_view(url='/artworks/')),
    url(r'^page/(?P<page>\d+)/$', 'artworks.views.artwork_list', name='artwork_list'),

    # /artworks/author/username/
    # /artworks/author/username/page/2/
    url(r'^author/(?P<username>[A-Za-z0-9_\-]+)/$', 'artworks.views.author_detail', name='author_detail'),
    url(r'^author/(?P<username>[A-Za-z0-9_\-]+)/page/1/$', AuthorRedirectView.as_view()),
    url(r'^author/(?P<username>[A-Za-z0-9_\-]+)/page/(?P<page>\d+)/$', 'artworks.views.author_detail', name='author_detail'),

    # /artworks/author/username/123/
    url(r'^author/(?P<username>[A-Za-z0-9_\-]+)/(?P<pk>\d+)/$', 'artworks.views.author_artwork_detail', name='author_artwork_detail'),

    # /artworks/123/
    url(r'^(?P<pk>\d+)/$', 'artworks.views.artwork_detail', name='artwork_detail'),

    # /artworks/project-slug/
    # /artworks/project-slug/page/2/
    url(r'^(?P<project>[A-Za-z0-9_\-]+)/$', 'artworks.views.project_detail', name='project_detail'),
    url(r'^(?P<project>[A-Za-z0-9_\-]+)/page/1/$', ProjectDetailRedirectView.as_view()),
    url(r'^(?P<project>[A-Za-z0-9_\-]+)/page/(?P<page>\d+)/$', 'artworks.views.project_detail', name='project_detail'),

    # /artworks/project-slug/123/
    url(r'^(?P<project>[A-Za-z0-9_\-]+)/(?P<pk>\d+)/$', 'artworks.views.project_artwork_detail', name='project_artwork_detail'),
]
