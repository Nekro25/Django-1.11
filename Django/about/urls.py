from django.conf.urls import url
from .views import description

urlpatterns = [
    url('', description),
]