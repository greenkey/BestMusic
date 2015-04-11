"""
BestMusic is a library to get music charts

"""


__author__ = "Lorenzo Mele"
__credits__ = ["Lorenzo Mele"]
__license__ = "GPL"
__version__ = "0.1"
__email__ = "lorenzo.mele@agavee.com"


import sys, os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from bestmusic import ProviderClass, ChartItem


class Provider(ProviderClass):
    myIdName = 'mockProvider2'
     
    def getChart(self, year):
        self.addItem(
            artist = 'Dolphins',
            title = 'So Long, and Thanks for All the Fish',
            score = 100/1,
            id = '1'
        )
        self.addItem(
            artist = 'Led Zeppelin',
            title = 'Stairway to Heaven',
            score = 100/2,
            id = '2'
        )
        self.addItem(
            artist = 'Dire Straits',
            title = 'Romeo and Juliet',
            score = 100/3,
            id = '3'
        )
        self.addItem(
            artist = 'Dire Straits',
            title = 'Romeo and Juliet',
            score = 100/4,
            id = '3'
        )
        return self.chart
