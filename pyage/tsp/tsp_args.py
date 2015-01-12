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
        print args

        if len(args) < 5:
            raise ValueError("Not enough parameters!")

        emas = args[3] == '1'
        logger.debug("Emas: " + str(emas))

        prob = float(args[4])
        logger.debug("Probability: " + str(prob))

        func = int(args[5])
        logger.debug("Mutation: " + str(func))

        return [emas, prob, func]