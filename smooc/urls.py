from django.conf.urls import url, include
from django.contrib import admin
from smooc.core import urls as core

urlpatterns = [
    url(r'^', include(core, namespace='core')),
    url(r'^admin/', admin.site.urls)
]
