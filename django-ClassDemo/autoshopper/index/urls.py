from django.conf.urls import url
from index.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^create_car_form', create_car_form),
    url(r'^randomize', randomize),
]