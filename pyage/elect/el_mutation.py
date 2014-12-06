import logging
import random
from pyage.core.operator import Operator
from pyage.elect.el_genotype import Votes

logger = logging.getLogger(__name__)

class AbstractMutation(Operator):
    def __init__(self, type, probability):
        super(AbstractMutation, self).__init__()
        self.probability = probability

    def process(self, population):
        for genotype in population:
            if random.random() < self.probability:
                self.mutate(genotype)

class Mutation(AbstractMutation):
    def __init__(self, probability=0.1):
        super(Mutation, self).__init__(Votes, probability)

    def mutate(self, genotype):
        logger.debug("MUT OF G:{0}".format(genotype.__hash__()))
        for vote in genotype.votes:
            rand = random.random()
            index_of_cand = vote.index(genotype.candidate)
            if rand < 0.5:
               # print "Mutation of vote: {0}".format()
                bias = random.randint(0,10) - 5
                biased = (index_of_cand-bias)%len(vote)
                vote.insert(biased, vote.pop(index_of_cand))
#                vote[index_of_cand], vote[biased] = vote[biased], vote[index_of_cand]
        logger.debug("Mutated and is now: {0}".format(genotype))
				
		
