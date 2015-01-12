# coding=utf-8
import sys
from pyage.tsp.tsp_generate_cities import TSPCitiesGenerator

__author__ = 'Michał Ciołczyk'

# Parameters

emas = [False, True]
emas_count = 10

mutation_prob = [0.01, 0.03, 0.1]
mutation_func = [0, 1]

generate = False
filename = ""

# Main routine

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage (without generation): python run.py <filename-with-cities>"
        print "Usage (with generation) python run.py generate <filename-to-save-cities-to> <number-of-cities>"
        exit(1)
    if sys.argv[1] == 'generate':
        generate = True
        filename = sys.argv[2]
    else:
        filename = sys.argv[1]
    if generate:
        generator = TSPCitiesGenerator(filename, int(sys.argv[3]))
        generator.generate()
    for e in emas:
        for pr in mutation_prob:
            for m in mutation_func:
                pass