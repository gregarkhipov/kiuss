from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from artworks.views import *

urlpatterns = patterns('',
    # /artworks/
    # /artworks/page/2/
    url(r'^$', 'artworks.views.ArtworkList', name='ArtworkList'),
    (r'^page/1/$', RedirectView.as_view(url='/artworks/all/')),
    url(r'^page/(?P<page>\d+)/$', 'artworks.views.ArtworkList', name='ArtworkList'),

    # /artworks/author/username/
    url(r'^author/(?P<username>[A-Za-z0-9_\-]+)/$', 'artworks.views.AuthorDetail', name='AuthorDetail'),
    (r'^author/(?P<username>[A-Za-z0-9_\-]+)/page/1/$', AuthorRedirectView.as_view()),
    url(r'^author/(?P<username>[A-Za-z0-9_\-]+)/page/(?P<page>\d+)/$', 'artworks.views.AuthorDetail', name='AuthorDetail'),
    # /artworks/author/username/123/
    url(r'^author/(?P<username>[A-Za-z0-9_\-]+)/(?P<pk>\d+)/$', 'artworks.views.AuthorArtworkDetail', name='AuthorArtworkDetail'),

    # /artworks/123/
    # /artworks/123/title-slug/
    url(r'^(?P<pk>\d+)/$', 'artworks.views.ArtworkDetail', name='ArtworkDetail'),
    url(r'^(?P<pk>\d+)/(?P<slug>[A-Za-z0-9_\-]+)/$', 'artworks.views.ArtworkDetail', name='ArtworkDetail'),

    # /artworks/project-slug/
    # /artworks/project-slug/page/2/
    url(r'^(?P<project>[A-Za-z0-9_\-]+)/$', 'artworks.views.ProjectDetail', name='ProjectDetail'),
    (r'^(?P<project>[A-Za-z0-9_\-]+)/page/1/$', ProjectDetailRedirectView.as_view()),
    url(r'^(?P<project>[A-Za-z0-9_\-]+)/page/(?P<page>\d+)/$', 'artworks.views.ProjectDetail', name='ProjectDetail'),
    # /artworks/project-slug/123/
    url(r'^(?P<project>[A-Za-z0-9_\-]+)/(?P<pk>\d+)/$', 'artworks.views.ProjectArtworkDetail', name='ProjectArtworkDetail'),
)

