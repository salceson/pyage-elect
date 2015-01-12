# coding=utf-8
import random
from pyage.tsp.tsp_city import City

__author__ = 'Michał Ciołczyk'


class TSPCitiesGenerator(object):
    def __init__(self, filename, n):
        self.filename = filename
        self.n = n

    def generate(self):
        cities = []
        for i in xrange(self.n):
            cities.append(City("City " + str(i), random.randint(0, 1000), random.randint(0, 1000)))
        with open(self.filename, 'w') as f:
            f.write("City,X,Y\n")
            for c in cities:
                f.write(c.name + "," + str(c.x) + "," + str(c.y) + "\n")
            f.flush()
