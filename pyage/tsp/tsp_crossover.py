# coding=utf-8
import random
import logging

from pyage.core.operator import Operator
from pyage.tsp.tsp_genotype import TSPGenotype


__author__ = 'Michał Ciołczyk'

logger = logging.getLogger(__name__)


class AbstractCrossover(Operator):
    def __init__(self, type, size):
        super(AbstractCrossover, self).__init__(type)
        self.__size = size

    def process(self, population):
        parents = list(population)
        for i in range(len(population), self.__size):
            p1, p2 = random.sample(parents, 2)
            genotype = self.cross(p1, p2)
            population.append(genotype)


class TSPCrossover(AbstractCrossover):
    def __init__(self, size):
        super(TSPCrossover, self).__init__(TSPGenotype, size)

    def cross(self, p1, p2):
        logger.debug("Crossing: " + str(p1) + " and " + str(p2))

        parent1 = p1.list
        parent2 = p2.list

        index1 = random.randrange(0, len(parent1))
        index2 = random.randrange(0, len(parent1))
        if index1 > index2:
            tmp = index1
            index1 = index2
            index2 = tmp

        parent1fragment = parent1[index1:index2]
        parent2fragment = parent2

        for city in parent1fragment:
            parent2fragment.remove(city)
        genlist = parent1fragment + parent2fragment

        genotype = TSPGenotype(p1.cities)
        genotype.set_list(genlist)

        logger.debug("Crossed genotype: " + str(genotype))

        return genotype