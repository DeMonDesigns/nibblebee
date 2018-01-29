from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<userid>[\w.-@]*)$', views.view_profile, name='get_profile'),
    url(r'^settings/$', views.edit_profile, name='edit_profile'),
    url(r'^settings/change-password/$', views.change_password, name='change_password'),
    url(r'^settings/change-username/$', views.change_username, name='change_username')
    # url(r'^oauth/', include('social_django.urls', namespace='social')),
]
