from django.conf.urls import url

from . import views

app_name = "citation"

urlpatterns = [
    url(r'^$', views.citations, name='citation'),
    #url(r'^add/$', views.citations, name='citations'),
    #url(r'^add/$', views.citationscreate, name='citationscreate')
]
