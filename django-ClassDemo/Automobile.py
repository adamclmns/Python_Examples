import random, json
import pymongo
from bson.binary import Binary
import pickle

# This is so I can randomly generate some "automobiles" with real names and stuff... 
possible_makes = ['Ford', 'Chevrolet', 'GMC', 'Aston Martin', 'BMW', 'KIA', 'Honda', 'Dodge', 'Jeep', 'Toyota', 'Subaru', 'Mitsubishi']
possible_models = ['Astro', 'F-150', 'Mustang', 'Probe','Corvette','Z-71','Camaro','Malibu','V12','Vantage','Jimmy','Tahoe', 'Cruze', 'Sorento', 'Rio', 'Dart', 'Charger', 'Wrangler', 'Cherokee', 'Liberty', 'Impreza', 'Forester', 'Outlander', 'Stealth', 'FTO', 'Tracker', 'Lacer', 'Gallant']
possible_colors = ['Red','Blue','White','Black','Silver','Grey','Orange','Lime Green','Green','Yellow','Purple']

class Automobile():
    # docstring
    def __init__(self, make=None, model=None, year=None, color=None):
        # docstring
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self._condition = 100
        self._mileage = 0
        self._crashes = 0


if __name__ == '__main__':
    # make a bunch of automobiles of different types...
    # Make 10 cars each time this is run

    db = pymongo.MongoClient().autoshopper
    for i in range(10):
        make = random.choice(possible_makes)
        model = random.choice(possible_models)
        color = random.choice(possible_colors)
        my_new_car = Automobile(make=make, model=model, year=2017, color=color)
        db.autos.insert(json.dumps(my_new_car))
