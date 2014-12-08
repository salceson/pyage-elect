import random
from pyage.core.emas import EmasAgent
from pyage.core.operator import Operator
from pyage.elect.el_genotype import Votes
import random

def emas_initializer(votes,candidate=1, energy=10, size=100):
    agents = {}
    for i in range(size):
        agent = EmasAgent(Votes(votes, candidate), energy, str(i))
        agents[agent.get_address()] = agent
    return agents

def root_agents_factory(count, type):
    def factory():
        agents = {}
        for i in range(count):
            agent = type('R' + str(i))
            agents[agent.get_address()] = agent
        return agents

    return factory

class VotesInitializer(object):

    def __init__(self, candidates_nr, voters_nr, c_nr, seed):
        self.candidates_nr = candidates_nr
        self.voters_nr = voters_nr
        random.seed(seed)
        self.c_nr = c_nr

    def __call__(self):
        basis = range(1,self.candidates_nr+1)
        votes_list = [(random.shuffle(basis), list(basis))[1] for _ in xrange(self.voters_nr)]
        c_places_list = [vote.index(self.c_nr) for vote in votes_list]
        return votes_list, c_places_list