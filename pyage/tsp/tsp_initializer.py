# coding=utf-8
import random
from pyage.core.emas import EmasAgent
from pyage.core.inject import Inject
from pyage.core.operator import Operator
from pyage.elect.el_genotype import Votes
from pyage.tsp.tsp_city import City
from pyage.tsp.tsp_genotype import TSPGenotype

__author__ = "Michał Ciołczyk"


class EmasInitializer(object):
    def __init__(self, votes, candidate, energy, size):
        self.votes = votes
        self.candidate = candidate
        self.energy = energy
        self.size = size

    @Inject("naming_service")
    def __call__(self):
        agents = {}
        for i in range(self.size):
            agent = EmasAgent(Votes(self.votes, self.candidate), self.energy, self.naming_service.get_next_agent())
            agents[agent.get_address()] = agent
        return agents


class TSPInitializer(Operator):
    def __init__(self, population_size=1000, filename=None, random_cities=False, random_cities_number=20):
        super(TSPInitializer, self).__init__(TSPGenotype)
        self.size = population_size
        if filename:
            self.cities = self.get_cities_from_file(filename)
            self.population = self.generate_population(population_size, self.cities)
        if random_cities:
            self.cities = self.generate_random_cities(random_cities_number)
            self.population = self.generate_population(population_size, self.cities)

    def __call__(self, *args, **kwargs):
        return self.population

    def process(self, population):
        for i in range(self.size):
            population.append(self.population[i])

    def generate_population(self, number_of_genotypes, cities):
        return [TSPGenotype(cities) for _ in xrange(0, number_of_genotypes)]

    def generate_random_cities(self, number_of_cities):
        cities = []
        for i in xrange(number_of_cities):
            cities.append(City("City " + str(i), random.randint(0, 1000), random.randint(0, 1000)))
        return cities

    def get_cities_from_file(self, filename):
        cities = []
        with open(filename, "r") as input:
            input.readline()  # skip first line
            for line in input:
                name, x, y = line.strip().split(",")
                cities.append(City(name, x, y))
        return cities

