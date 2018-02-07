"""nibble_bee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ck_views

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^users/', include('users.urls')),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^ckeditor/upload/', ck_views.upload, name='ckeditor_upload'),
    url(r'^ckeditor/browse/', never_cache(ck_views.browse), name='ckeditor_browse'),
]

# original urls
# url(r'^upload/', staff_member_required(views.upload), name='ckeditor_upload'),
# url(r'^browse/', never_cache(staff_member_required(views.browse)), name='ckeditor_browse'),

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
