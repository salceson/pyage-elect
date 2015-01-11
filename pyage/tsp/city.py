# coding=utf-8
__author__ = 'Michał Ciołczyk'


class City(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return "City{name=" + self.name + ", x=" + self.x + ", y=" + self.y + "}"
