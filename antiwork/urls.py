from django.conf.urls import include, url
from django.contrib import admin
import main

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from antiwork import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^', include('main.urls')),
]