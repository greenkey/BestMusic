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
        return self.providers[0].getChart(year=year)


class ProviderClass:

    def getChart(self=None, year=None):
        return []

    def normalizeChart(self=None, chart=None):
        return chart

