
from django.conf.urls import url
from smooc.core.views import home, contact

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contato/$', contact, name='contact'),
]
