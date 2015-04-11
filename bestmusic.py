#!/usr/bin/env python3

"""
BestMusic is a library to get music charts

"""


__author__ = "Lorenzo Mele"
__credits__ = ["Lorenzo Mele"]
__license__ = "GPL"
__version__ = "0.1"
__email__ = "lorenzo.mele@agavee.com"

class BestMusic:
    providers = list()

    def __init__(self):
        import pkgutil
        import providers
        from importlib import import_module
        for importer, modname, ispkg in pkgutil.iter_modules(providers.__path__):
            self.providers.append( import_module('providers.' + modname).Provider() )
     
    def getChart(self, year=None):
        chart = list()
        for p in self.providers:
            chart.extend(p.getChart(year=year))
        return self.normalizeChart(chart)

    def normalizeChart(self, chart):
        for p in self.providers:
            chart = p.normalizeChart(chart)
        return chart



class ProviderClass:
    idName = 'not_set'
    chart = None

    def __init__(self):
        self.chart = list()

    def getChart(self, year):
        return self.chart

    def normalizeChart(self, chart):
        newchart = list()
        for i in chart:
            found = False
            for j in newchart:
                try:
                    if i.ids[self.idName] == j.ids[self.idName]:
                        found = True
                        j.addScore(i.getScore())
                except(KeyError):
                    pass
            if not found:
                newchart.append(i)
        return newchart

    def addItem(self, artist, title, score, sourceId):
        self.chart.append(ChartItem(
            artist = artist,
            title = title,
            score = score,
            sourceId = sourceId,
            source = self.idName
        ))


class ChartItem:
    artist = None
    title = None
    scores = None
    ids = None

    def __init__(self, artist, title, score, sourceId, source):
        self.artist = artist
        self.title = title
        self.scores = list()
        self.addScore(score)
        self.ids = dict()
        self.ids[source] = sourceId

    def addScore(self, score):
        self.scores.append(score)

    def setId(self, sourceId, source):
        self.ids[source] = sourceId

    def getScore(self):
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return "ids:{}; artist:{}; title={}".format(self.ids, self.artist, self.title)