# coding=utf-8
import random
import logging

from pyage.core.operator import Operator
from pyage.tsp.tsp_genotype import TSPGenotype


__author__ = 'Michał Ciołczyk'

logger = logging.getLogger(__name__)


class AbstractMutation(Operator):
    def __init__(self, type=TSPGenotype, probability=0.5):
        super(AbstractMutation, self).__init__(type)
        self.probability = probability

    def process(self, population):
        for genotype in population:
            if random.random() < self.probability:
                self.mutate(genotype)


class TSPMutation1(AbstractMutation):
    def __init__(self, probability):
        super(TSPMutation1, self).__init__(TSPGenotype, probability)

    def mutate(self, genotype):
        logger.debug("Mutating (rand swap) genotype: " + str(genotype))

        l = genotype.list
        index1 = random.randrange(0, len(l))
        index2 = random.randrange(0, len(l))
        e1 = l[index1]
        e2 = l[index2]
        l[index2] = e1
        l[index1] = e2
        gen = TSPGenotype(genotype.cities)
        gen.set_list(l)

        logger.debug("Mutated (rand swap) genotype: " + str(gen))

        return gen


class TSPMutation2(AbstractMutation):
    def __init__(self, probability):
        super(TSPMutation2, self).__init__(TSPGenotype, probability)

    def mutate(self, genotype):
        logger.debug("Mutating (next swap) genotype: " + str(genotype))

        l = genotype.list
        index1 = random.randrange(0, len(l))
        index2 = (index1 + 1) % len(l)
        e1 = l[index1]
        e2 = l[index2]
        l[index2] = e1
        l[index1] = e2
        gen = TSPGenotype(genotype.cities)
        gen.set_list(l)

        logger.debug("Mutated (next swap) genotype: " + str(gen))

        return gen