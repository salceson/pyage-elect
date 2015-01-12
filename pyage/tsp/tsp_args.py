# coding=utf-8
import sys
import logging

__author__ = 'Michał Ciołczyk'

logger = logging.getLogger(__name__)


class ArgumentParser(object):
    def __init__(self):
        pass

    @staticmethod
    def parse_args():
        args = sys.argv

        if len(args) < 6:
            raise ValueError("Not enough parameters!")

        emas = args[3] == '1'
        logger.debug("Emas: " + str(emas))

        prob = float(args[4])
        logger.debug("Probability: " + str(prob))

        func = int(args[5])
        logger.debug("Mutation: " + str(func))

        filename = args[6]

        return [emas, prob, func, filename]