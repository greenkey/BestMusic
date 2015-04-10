"""
BestMusic is a library to get music charts

"""


__author__ = "Lorenzo Mele"
__credits__ = ["Lorenzo Mele"]
__license__ = "GPL"
__version__ = "0.1"
__email__ = "lorenzo.mele@agavee.com"


class Provider:
     
   def getChart(self, year=None):
        return [
            {
                'artist': 'Dolphins',
                'title': 'So Long, and Thanks for All the Fish'
            },{
                'artist': 'Led Zeppelin',
                'title': 'Stairway to Heaven'
            },{
                'artist': 'Dire Straits',
                'title': 'Romeo and Juliet'
            }
        ]

