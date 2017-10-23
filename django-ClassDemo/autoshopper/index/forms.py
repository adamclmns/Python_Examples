from django import forms


class AutoForm(forms.Form):
    make = forms.CharField(label='Manufacturer: ', max_length=100)
    model = forms.CharField(label="Model", max_length=100)
    color = forms.CharField(label="Ccolor", max_length=100)
    year = forms.CharField(label="Year", max_length=4)
    mileage = forms.CharField(label="Mileage", max_length=9)
    