from django.conf.urls import patterns, include, url
from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import pdb


def debug(request):
    pdb.set_trace()
    return HttpResponse()

urlpatterns = patterns('',
    url(r'.*', debug)
)
