# coding=utf-8
import logging
from matplotlib.pyplot import errorbar, savefig
from numpy import average, std
import os
from pyage.core.statistics import Statistics

__author__ = "Michał Ciołczyk"

logger = logging.getLogger(__name__)


class StepStatisticsWithStdDev(Statistics):
    def __init__(self, output_file_name='fitness_pyage.txt', plot_file_name='plot.png', take_max_as_best=True):
        self.history = []
        self.fitness_output = open(output_file_name, 'a')
        self.take_max_as_best = take_max_as_best
        self.plot_file_name = plot_file_name

    def __del__(self):
        self.fitness_output.close()

    def append(self, best_fitness, step_count):
        self.fitness_output.write(str(step_count - 1) + ';' + str(best_fitness) + '\n')
        self.fitness_output.flush()
        os.fsync(self.fitness_output)

    def update(self, step_count, agents):
        try:
            fitnesses = [a.get_fitness() for a in agents]
            best_fitness = max(fitnesses) if self.take_max_as_best else min(fitnesses)
            avg_fitness = average(fitnesses)
            std_dev = std(fitnesses)
            logger.debug(best_fitness)
            self.history.append((best_fitness, avg_fitness, std_dev))
            if (step_count - 1) % 100 == 0:
                self.append(best_fitness, step_count)
        except:
            logging.exception("")

    def summarize(self, agents):
        try:
            logger.debug(self.history)
            best_agent = max(agents, key=lambda a: a.get_fitness())
            best_genotype = best_agent.get_best_genotype()
            self.fitness_output.write("best genotype:\n%s" % best_genotype)
            self.fitness_output.close()
            average = []
            std_dev = []
            for (best, avg, stddev) in self.history:
                average.append(avg)
                std_dev.append(stddev)
            steps = range(1, len(average) + 1)
            logger.debug("Size: " + str(len(average)))
            logger.debug(average)
            logger.debug(std_dev)
            logger.debug("Plotting results: errorbar")
            errorbar(steps, average, std_dev)
            logger.debug("Plotting results: savefig")
            savefig(self.plot_file_name)
            logger.debug("Done!")
        except Exception as e:
            logging.exception(e)

