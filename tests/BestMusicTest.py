###############################################################################
# test
import unittest
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from bestmusic import BestMusic


class TestBestMusic(unittest.TestCase):
    bm = BestMusic()

    def test_chart(self):
        self.chart = self.bm.getChart(year=1971)
        self.assertNotEqual(len(chart), 0)
        for i in range(len(chart)):
            self.assertIsNotNone(chart[i]['artist'])
            self.assertIsNotNone(chart[i]['title'])

    def test_normalization(self):
        normChart = self.bm.normalizeChart(chart=self.chart)
        self.assertNoEqual(len(normChart), 0)


if __name__ == '__main__':
    unittest.main()