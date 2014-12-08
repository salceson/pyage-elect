import random
from pyage.core.operator import Operator
from pyage.elect.el_genotype import Votes

import logging

logger = logging.getLogger(__name__)

class Crossover(object):

    def cross(self, p1, p2):
        logger.debug("Crossing: {0} and {1}".format(p1, p2))
        division = random.randint(1, len(p1.votes)-2)
        new_votes = p1.votes[:division] + p2.votes[division:]
        #logger.debug("new votes:" + str(new_votes))
        return Votes(new_votes, p1.candidate)

