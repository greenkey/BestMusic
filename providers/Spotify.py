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

from submodules.spotipy import spotipy

class Provider(ProviderClass):
    idName = 'Spotify'
    sp = spotipy.Spotify()

    def normalizeChart(self, chart):
        for item in chart:
            # search for the song
            pass
            
        return ProviderClass.normalizeChart(self, self.chart)