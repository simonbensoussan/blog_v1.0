from django.conf.urls import url
from django.contrib import admin
from . import views

app_name ='post'

urlpatterns = [
   # /post/
    url(r'^$', views.postList, name='list'),

    #CRUD :

    url(r'^create/$', views.postCreate, name='create'),
    # /post/<id_of_object>
    url(r'^(?P<id>\d+)/$', views.postDetail, name='detail'), #regex for the id only the number dynamic url
    url(r'^(?P<id>\d+)/edit/$', views.postUpdate, name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.postDelete, name='delete'),
#   url(r'^$', "<app_name>.views.<function_name>"), best method

]
