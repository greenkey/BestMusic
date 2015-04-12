###############################################################################
# test
import unittest
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from bestmusic import BestMusic, ProviderClass


class TestBestMusic(unittest.TestCase):

    def test_chart(self):
        bm = BestMusic(useMock=True)
        chart = bm.getChart(year=1971)
        self.assertNotEqual(len(chart), 0)
        for i in range(len(chart)):
            self.assertIsNotNone(chart[i].artist)
            self.assertIsNotNone(chart[i].title)

    def test_sort(self):
        bm = BestMusic(useMock=True)
        chart = bm.getChart(year=1971)
        prevScore = chart[0].getScore()
        for item in chart[1:]:
            self.assertTrue(item.getScore() <= prevScore)
            prevScore = item.getScore()

class TestProvider(unittest.TestCase):

    def test_getChart(self):
        p = ProviderClass()
        chart = p.getChart(year=1971)
        self.assertEqual(chart, [])

    def test_normalization(self):
        p = ProviderClass()
        p.addItem('artist','title',1,'sourceId')
        p.addItem('artist','title',3,'sourceId')
        chart = p.getChart(year=1971)
        chart = p.normalizeChart(chart)
        self.assertEqual(len(chart), 1)

    def test_addItem(self):
        p = ProviderClass()
        chart = p.getChart(year=1971)
        l = len(chart)
        p.addItem('artist','title',1,'sourceId')
        self.assertEqual(l+1, len(chart))

    def test_sort(self):
        p = ProviderClass()
        p.addItem('artist','title',3,'2')
        p.addItem('artist','title',3,'7')
        p.addItem('artist','title',3,'0')
        p.addItem('artist','title',3,'23')
        p.addItem('artist','title',1,'1')
        p.sort()
        chart = p.getChart(year=1971)
        prevScore = chart[0].getScore()
        for item in chart[1:]:
            self.assertTrue(item.getScore() <= prevScore)
            prevScore = item.getScore()


if __name__ == '__main__':
    unittest.main()