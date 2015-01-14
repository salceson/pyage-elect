# coding=utf-8

from matplotlib import pyplot as plt
from pyage.tsp.tsp_city import City

__author__ = 'Michał Ciołczyk'


def plot_cities(cities, canvas):
    """ Plots cities on canvas

    @param cities: list of cities to plot
    @param canvas: canvas to plot on
    """
    for (x, y) in cities:
        canvas.plot(x, y, 'ro')
        plt.draw()


def draw_path(cities, canvas, width, height):
    """ Draws cities with paths

    @param cities: list of cities to plot
    @param canvas: canvas to plot on
    @param width: width of image
    @param height: height of image
    """
    plt.ion()
    canvas.clear()
    canvas.set_xlim(0, width)
    canvas.set_ylim(0, height)
    plot_cities(cities, canvas)

    n = len(cities)
    (x1, y1) = cities[0]
    for i in xrange(1, n + 1):
        (x2, y2) = cities[i % n]
        canvas.plot([x1, x2], [y1, y2], color='r', linestyle='-', linewidth=0.4)
        (x1, y1) = (x2, y2)
    plt.pause(0.01)
    plt.ioff()
    plt.savefig("troll.png")


def get_cities_from_file(filename):
    cities = []
    with open(filename, "r") as input:
        input.readline()  # skip first line
        for line in input:
            name, x, y = line.strip().split(",")
            cities.append(City(name, int(x), int(y)))
    return cities


if __name__ == "__main__":
    width = 1200
    height = 1200
    genotype = [28, 3, 17, 0, 11, 29, 9, 22, 19, 6, 7, 1, 12, 15, 27, 14, 8, 25, 21, 5, 16, 23, 4, 24, 26, 2, 20, 10,
                18, 13]
    filename = "cities.csv"

    cities_list = get_cities_from_file(filename)

    fig = plt.figure()
    canvas = fig.add_subplot(111)

    c = [cities_list[i] for i in genotype]
    cities = [(city.x, city.y) for city in c]

    draw_path(cities, canvas, width, height)