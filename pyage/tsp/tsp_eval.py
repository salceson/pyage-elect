# coding=utf-8
import logging

from pyage.core.operator import Operator
from pyage.tsp.tsp_genotype import TSPGenotype


__author__ = 'Michał Ciołczyk'

logger = logging.getLogger(__name__)


class TSPEvaluator(Operator):
    def __init__(self):
        super(TSPEvaluator, self).__init__(TSPGenotype)

    def process(self, population):
        for genotype in population:
            genotype.fitness = self.evaluate(genotype)

    def evaluate(self, genotype):
        return genotype.calculate_fitness()