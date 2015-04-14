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

import cachetools

class Provider(ProviderClass):
    idName = 'Spotify'
    sp = spotipy.Spotify()

    def normalizeChart(self, chart):
        for item in chart:
            print('-------------------------')
            print(item)
            song = self.getSongData(item.title, item.artist)
            if song:
                item.title = song['name']
                item.artist = song['artists'][0]['name']
                item.addId(song['id'], self.idName)
            print(item)
        return ProviderClass.normalizeChart(self, chart)

    @cachetools.ttl_cache(maxsize=2048, ttl=7*24*60*60) #cached for 1 week
    def getSongData(self, title, artist):
        # search for the song
        artists = artist.replace('featuring',';').replace('&',';').replace('and',';').split(';')
        results = self.sp.search(
            q=artists[0]+' '+title, 
            limit=20
        )
        for i, t in enumerate(results['tracks']['items']):
            # TODO: place a real algorithm
            return t
