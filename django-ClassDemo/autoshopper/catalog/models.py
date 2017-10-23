"""models module for the index and catalog app"""
from mongoengine import DynamicDocument, StringField
# Create your models here.

class Auto(DynamicDocument):
    """Mongo DB Object for Autoshopper. This object is shared with the Catalog and Index Apps"""
    make = StringField(max_length=100)
    model = StringField(max_length=100)
    color = StringField(max_length=100)
    year = StringField(max_length=4)
    mileage = StringField(max_length=9)
    