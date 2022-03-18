from django.conf.urls import url, include
from .views import user_list, user_detail, profile, signup

user = [
    url(r'^(?P<item>[\d]+)/$', user_detail),
    url('', user_list),
]


urlpatterns = [
    url('users/', include(user)),
    url('signup/', signup),
    url('profile/', profile),
]