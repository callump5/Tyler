from django.conf.urls import url

from .views import get_base, get_services, get_service
urlpatterns = [

    # Home
    url(r'^$', get_base, name='home'),

    # Services
    url(r'^services/$', get_services, name='services'),
    url(r'^services/(?P<service_id>\d+)/$', get_service, name='service')
]