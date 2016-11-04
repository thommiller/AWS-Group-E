from django.conf.urls import url

from . import views

app_name = "citation"

urlpatterns = [
    url(r'^$', views.citations, name='citations'),
    url(r'^citations_data$', views.citations_data, name='citations_data'),
    #url(r'^add/$', views.citations, name='citations'),
    #url(r'^add/$', views.citationscreate, name='citationscreate')
]
