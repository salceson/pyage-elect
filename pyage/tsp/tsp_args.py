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
        ret_val = []

        if len(args) < 4:
            raise ValueError("Not enough parameters!")

        emas = args[2] == 'emas'
        logger.debug("Emas: " + str(emas))

        return ret_val