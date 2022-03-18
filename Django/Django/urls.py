from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('catalog/', include('catalog.urls')),
    url('about/', include('about.urls')),
    url('auth/', include('users.urls')),
    url('', include('homepage.urls')),
]