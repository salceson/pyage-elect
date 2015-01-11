# coding=utf-8
import logging

from pyage.core import address
from pyage.core.agent.agent import generate_agents, Agent
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition
from pyage.elect.naming_service import NamingService
from pyage.tsp.tsp_eval import TSPEvaluator
from pyage.tsp.tsp_initializer import TSPInitializer
from pyage.tsp.tsp_selection import TournamentSelection
from pyage.tsp.tsp_crossover import TSPCrossover
from pyage.tsp.tsp_mutation import TSPMutation1

__author__ = "Michał Ciołczyk"

logger = logging.getLogger(__name__)

agents_count = 1
logger.debug("EVO, %s agents", agents_count)
# logger.debug("EMAS, %s agents", agents_count)
# agents = root_agents_factory(agents_count, AggregateAgent)
agents = generate_agents("agent", agents_count, Agent)

stop_condition = lambda: StepLimitStopCondition(20)

size = 10
random_cities = 30
population_size = 130
operators = lambda: [TSPEvaluator(), TournamentSelection(size=125, tournament_size=125),
                     TSPCrossover(size=size), TSPMutation1(probability=0.03)]
initializer = lambda: TSPInitializer(population_size=population_size, random_cities=True,
                                      random_cities_number=random_cities)

# agg_size = 40
# aggregated_agents = EmasInitializer(votes=votes, candidate = chosen_candidate, size=agg_size, energy=40 )
#
# emas = EmasService

# minimal_energy = lambda: 10
# reproduction_minimum = lambda: 100
# migration_minimum = lambda: 120
# newborn_energy = lambda: 100
# transferred_energy = lambda: 40

# budget = 0
# evaluation = lambda: kApprovalEvaluator(k_approval_coeff,[simple_cost_func]*votes_nr,budget, init_c_places, chosen_candidate)
# crossover = lambda: Crossover(size=30)
# mutation = lambda: Mutation(probability=0.2, evol_probability=0.5)

# def simple_cost_func(x): return abs(x)*10


address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics('fitness_%s_pyage.txt' % __name__)

naming_service = lambda: NamingService(starting_number=2)