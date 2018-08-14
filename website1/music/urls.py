from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /Music/712/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),

    #used app for adding Albums and songs with the form, music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    #add music/song
    url(r'song/add/$', views.SongCreate.as_view(), name='song-add'),

    #/music/album/2/
    url(r'album(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name = 'album-update'),

    url(r'song(?P<pk>[0-9]+)/$', views.SongUpdate.as_view(), name = 'song-update'),

    #/music/album/2/delete/
    url(r'album(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name = 'album-delete'),


]
