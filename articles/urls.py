from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^all/$', views.all),
    url(r'^get/(?P<article_id>\d+)/$', views.get),
    url(r'^create/$', views.create),
]
