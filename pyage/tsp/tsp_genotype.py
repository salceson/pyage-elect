# coding=utf-8
import random

__author__ = 'Michał Ciołczyk'


class TSPGenotype(object):
    def __init__(self, cities):
        self.cities = cities
        self.n = len(cities)
        self.list = [x for x in xrange(0, self.n)]
        random.shuffle(self.list)
        self.fitness = self.calculate_fitness()

    def __str__(self):
        return "TSPGenotype{list=" + str(self.list) + ", fitness=" + str(self.fitness) + "}"

    def calculate_fitness(self):
        fitness = 0.0
        prev = self.list[0]
        for i in xrange(1, self.n + 1):
            i %= self.n
            index = self.list[i]
            delta_x = self.cities[index].x - self.cities[prev].x
            delta_y = self.cities[index].y - self.cities[prev].y
            fitness -= delta_x ** 2 + delta_y ** 2
            prev = index
        return fitness

    def set_list(self, list):
        self.list = list
        self.fitness = self.calculate_fitness()