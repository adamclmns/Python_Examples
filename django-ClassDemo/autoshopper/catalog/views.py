"""
Views for Autoshopper Catalog
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.serializers import serialize
from catalog.models import Auto

# Create your views here.
def index(request):
    """
    index page for catalog
    """
    autos = Auto.objects()
    return render(request, 'catalog.html', {'autos':autos})


