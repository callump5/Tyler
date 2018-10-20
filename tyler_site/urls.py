from django.conf.urls import url

from .views import get_base
urlpatterns = [
    url(r'^$', get_base)
]