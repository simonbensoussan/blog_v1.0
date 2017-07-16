from django.conf.urls import url
from django.contrib import admin
from . import views

app_name ='portfolio'

urlpatterns = [
   # /post/
    url(r'^$', views.home, name='home'),
]
