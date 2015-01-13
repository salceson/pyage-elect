# coding=utf-8
from matplotlib.pyplot import errorbar, savefig, legend, title

__author__ = 'Michał Ciołczyk'


avg1 = []
stddev1 = []
avg2 = []
stddev2 = []
avg3 = []
stddev3 = []

basedir = "plots/"
plotname = ""
extension = ".png"

avgs = []
stddevs = []

legends = ["", "", ""]
t = ""

if len(avg1) > 0:
    avgs.append(avg1)
    stddevs.append(stddev1)

if len(avg2) > 0:
    avgs.append(avg2)
    stddevs.append(stddev2)

if len(avg3) > 0:
    avgs.append(avg3)
    stddevs.append(stddev3)

for i in xrange(len(avgs)):
    errorbar(range(1, len(avgs[i]) + 1), avgs[i], stddevs[i], label=legends[i])

title(t)
legend()
savefig(basedir + plotname + extension)