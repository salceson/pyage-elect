# coding=utf-8
import logging
import os
import math

from pyage.core import address

from pyage.core.agent.agent import unnamed_agents
from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition

from pyage.elect.el_crossover import Crossover
from pyage.elect.el_eval import kApprovalEvaluator 
from pyage.elect.el_init import emas_initializer 
from pyage.elect.el_mutation import Mutation


votes = [
	[5,4,3,2,1],
	[5,2,3,4,1],
	[3,4,5,2,1],
	[1,2,3,5,4],
	[3,1,4,5,2],
	[5,2,1,4,3],
]

votes_nr = len(votes)

logger = logging.getLogger(__name__)

agents_count = 5
logger.debug("EMAS, %s agents", agents_count)
agents = unnamed_agents(agents_count, AggregateAgent)

stop_condition = lambda: StepLimitStopCondition(10000)

aggregated_agents = lambda: emas_initializer(votes = votes, candidate = 1,size=40, energy=40 )

emas = EmasService

minimal_energy = lambda: 0
reproduction_minimum = lambda: 90
migration_minimum = lambda: 120
newborn_energy = lambda: 100
transferred_energy = lambda: 40

evaluation = lambda: kApprovalEvaluator(2,[lambda x:abs(x)*10]*votes_nr,50, [4,4,4,0,1,2])
crossover = lambda: Crossover(size=50)
mutation = lambda: Mutation(probability=0.75)

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics('fitness_%s_pyage.txt' % __name__)
