import random
from pyage.core.emas import EmasAgent
from pyage.core.operator import Operator
from pyage.elect.el_genotype import Votes

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

