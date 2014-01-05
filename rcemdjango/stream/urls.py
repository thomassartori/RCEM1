from django.conf.urls import patterns, url

from stream import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^message/add$', views.add_message, name='add_message')
)