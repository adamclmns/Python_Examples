
"""
Views Module for the Index App
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import AutoForm
from index.models import Auto
import json
import random


# Create your views here.

def index(request):
    """
    Index Page
    """
    return render(request, 'index.html', {})


def create_car_form(request):
    """This will bulid the form to create a new car object"""
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AutoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data)
            auto = Auto.from_json(json.dumps(form.cleaned_data))
            print(auto)
            auto.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/index/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AutoForm()

    return render(request, 'auto_form.html', {'form': form})


possible_makes = ['Ford', 'Chevrolet', 'GMC', 'Aston Martin', 'BMW',
                  'KIA', 'Honda', 'Dodge', 'Jeep', 'Toyota', 'Subaru', 'Mitsubishi']
possible_models = ['Astro', 'F-150', 'Mustang', 'Probe', 'Corvette', 'Z-71', 'Camaro', 'Malibu',
                   'V12', 'Vantage', 'Jimmy', 'Tahoe', 'Cruze', 'Sorento', 'Rio', 'Dart',
                   'Charger', 'Wrangler', 'Cherokee', 'Liberty', 'Impreza', 'Forester',
                   'Outlander', 'Stealth', 'FTO', 'Tracker', 'Lacer', 'Gallant']
possible_colors = ['Red', 'Blue', 'White', 'Black', 'Silver',
                   'Grey', 'Orange', 'Lime Green', 'Green', 'Yellow', 'Purple']


def randomize(request):
    for i in range(10):
        make = random.choice(possible_makes)
        model = random.choice(possible_models)
        color = random.choice(possible_colors)
        mileage = random.randint(0, 25000)
        year = random.randint(1990, 2018)

        auto = {
            "make": make,
            "model": model,
            "color": color,
            "mileage": str(mileage),
            "year": str(year)
        }
        Auto.from_json(json.dumps(auto)).save()
    return render(request, 'index.html', {})
