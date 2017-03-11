# Showing examples of nested for loops 
"""
height = int(input("height?  "))
width = int(input("width?  "))

# read as "For i from 0 to 'height'""
for i in range(height):
    # read as "For 'k' from 0 to 'width'"
    for k in range(width):
        # Python-Fu, print without a new line found here - http://stackoverflow.com/a/493399
        print("*", end="") # default end="\n"
    print('') # So we get a new line

#EXAMPLE
#  For loops are nice for checking over a list of things. 

pets = ["Dog","Cat","Gecko","Finch","Squirrel","Parrot","Ficus Tree","Goldfish",]

# read this as "For each 'animal' in 'pets', print 'animal'"
for animal in pets:
    print(animal)

# You can also iterate over strings

# Read this as "For each 'i' in 'Oh No, Don't Cut Me into Pieces!!!', print character"
for i in "Oh No, Don't Cut Me into Pieces!!!":
    print(i)

"""
# EXAMPLE
# I need 1000 random numbers to do stats on.
from random import randint
dataset = []

for i in range(1000):
    dataset.append(randint(0,250))


sum = sum(dataset) # Isn't that handy?
# Using a library to do stats
import statistics
print("Mean: %f" %statistics.mean(dataset))
try:
    print("Mode: %f" %statistics.mode(dataset))
except:
    print("found more than one equally common value... ")
print("Median: %f" %statistics.median(dataset))
print("Standard Deviation: %f" %statistics.stdev(dataset))
print("Variance: %f" %statistics.variance(dataset))
