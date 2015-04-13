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
from bestmusic import ProviderClass


class Provider(ProviderClass):
    idName = 'UKChartTopSource'
     
    def getChart(self, year):
        html = self.parseWebPage('http://www.uk-charts.top-source.info/top-100-' + str(year) + '.shtml')
        table = html.find(
            "div", { 'id' : 'ContentColumn' }).find(
            "table", { 'class' : 'sortable' })
        trs = table.findAll('tr')[1:]
        scoreK = len(trs)
        for tr in trs:
            row = tr.findAll('td')
            self.addItem(
                artist = row[1].text,
                title = row[2].text,
                score = scoreK / int(row[0].text),
                sourceId = str(year) + '-' + row[0].text
            )
        return self.chart

