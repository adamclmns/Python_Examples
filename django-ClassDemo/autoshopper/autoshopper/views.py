"""
Views for Autoshopper Root
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize


# Create your views here.
def index(request):
    """
    index page for root
    """
    return HttpResponseRedirect('/index/')


