"""urls module for the index App"""
from django.conf.urls import url
from catalog.views import index

urlpatterns = [
    url(r'^$', index),
]
