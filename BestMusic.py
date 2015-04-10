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




###############################################################################
# main

if __name__ == "__main__":
    from optparse import OptionParser
    from util.util import Logger

    ###########################################################################
    # parse parameters and init

    mylog = Logger()
    log = mylog.log

    parser = OptionParser()
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose", default=False,
                      help="print useful output for debugging")
    parser.add_option("--year",
                      dest="year",
                      help="set the year of analysis")


    (options, args) = parser.parse_args()

    mylog.setVerbose(options.verbose)

    log("options:")
    log(options)
    log("args:")
    log(args)

    ###########################################################################
    # 

    bm = BestMusic()

    if args[0] == "chart":

        chart = bm.getChart(year=options.year)

        print("Chart for year {}".format(options.year))
        for i in range(len(chart)):
            print("{}. {} - {}".format(
                i+1,
                chart[i]['artist'],
                chart[i]['title']
            ))