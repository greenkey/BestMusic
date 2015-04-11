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
        return chart

    def addItem(self, artist, title, score, id):
        self.chart.append(ChartItem(
            artist = artist,
            title = title,
            score = score,
            id = id,
            source = self.idName
        ))


class ChartItem:
    artist = None
    title = None
    scores = dict()
    ids = dict()

    def __init__(self, artist, title, score, id, source):
        self.artist = artist
        self.title = title
        self.scores[source] = score
        self.ids[source] = id

    def setScore(self, score, source):
        self.scores[source] = score

    def setId(self, id, source):
        self.ids[source] = id

    def getScore(self):
        return sum(self.scores.values()) / len(self.scores)