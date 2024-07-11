# Practical-9 Dictionary

# Given dictionary
# data = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}


# for name in name to score.key():
#    print(len(names))
#    sorting
# add the forloop
# dynamic with (It is not fixed)

############################################################################
# key is immutable(cannot have more than one)
# value is mutable (can change the value)
# dictionary is mutable


###########################################################################
# cannot find 1
# find +1

###########################################################################
# Write a function that takes a list o strings and returns a dictionary of
# string: length of string pairs.


###########################################################################
# Teamwork

# display countries
# used csv reader
# example to diffrent way of reading file
import csv

FILENAME = "countries.csv"


def load_countries_data(files_path):
    countries = []
    with open(files_path, mode='r') as file:
        reader = csv.DictReader(file)
