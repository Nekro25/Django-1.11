from django.conf.urls import url
from .views import item_list, item_detail

urlpatterns = [
    url(r'^(?P<item>[\d]+)/$', item_detail),
    url('', item_list),
]
