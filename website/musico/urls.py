from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^list/$', views.musico, name="musico"),
    url(r'^(?P<pk>[0-9]+)/$',views.listsong, name="list_song"),
    url(r'^settings/$',views.add_movie,name="settings"),
    url(r'^add-song/$',views.add_song,name="add-song"),
    ] 
