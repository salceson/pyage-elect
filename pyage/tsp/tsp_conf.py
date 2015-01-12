# coding=utf-8
import logging
import sys

from pyage.core import address
from pyage.core.agent.agent import generate_agents, Agent
from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.real_gnuplot import StepStatisticsWithStdDev
from pyage.core.stop_condition import StepLimitStopCondition
from pyage.tsp.tsp_naming_service import NamingService
from pyage.tsp.tsp_eval import TSPEvaluator
from pyage.tsp.tsp_initializer import TSPInitializer, root_agents_factory, EmasInitializer
from pyage.tsp.tsp_selection import TournamentSelection
from pyage.tsp.tsp_crossover import TSPCrossover
from pyage.tsp.tsp_mutation import TSPMutation1, TSPMutation2
from pyage.tsp.tsp_args import ArgumentParser

__author__ = "Michał Ciołczyk"

logger = logging.getLogger(__name__)

args = None

try:
    args = ArgumentParser.parse_args()
except ValueError as e:
    logger.debug(e.message)

use_emas = args[0]
mutation_prob = args[1]
mutation_func = args[2]
filename = args[3]

agents_count = 10

if use_emas:
    logger.debug("EMAS, %s agents", agents_count)
    agents = root_agents_factory(agents_count, AggregateAgent)
else:
    logger.debug("EVO, %s agents", agents_count)
    agents = generate_agents("agent", agents_count, Agent)

stop_condition = lambda: StepLimitStopCondition(1000)

if not use_emas:
    size = 130
    random_cities = 30
    population_size = 10000
    operators = lambda: [TSPEvaluator(), TournamentSelection(size=125, tournament_size=125),
                         TSPCrossover(size=size),
                         TSPMutation1(probability=mutation_prob) if mutation_func == 1
                         else TSPMutation2(probability=mutation_prob)]
    initializer = lambda: TSPInitializer(population_size=population_size, random_cities=False,
                                         filename=filename)

else:
    agg_size = 40
    aggregated_agents = EmasInitializer(filename=filename, size=agg_size, energy=40)

    emas = EmasService

    minimal_energy = lambda: 10
    reproduction_minimum = lambda: 100
    migration_minimum = lambda: 120
    newborn_energy = lambda: 100
    transferred_energy = lambda: 40

    budget = 0
    evaluation = lambda: TSPEvaluator()
    crossover = lambda: TSPCrossover(size=30)
    mutation = lambda: TSPMutation1(probability=mutation_prob) if mutation_func == 1 \
        else TSPMutation2(probability=mutation_prob)

    def simple_cost_func(x):
        return abs(x) * 10

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatisticsWithStdDev()

naming_service = lambda: NamingService(starting_number=1)