#!/usr/bin/python

"""
Useful things
"""

__author__ = "Lorenzo Mele"
__credits__ = ["Lorenzo Mele"]
__license__ = "GPL"
__version__ = "0.1"
__email__ = "lorenzo.mele@agavee.com"


class Logger(object):
    "Logger object, initialize to display print messages."

    verbose = False
    colour = '\033[90m'
    colourEnd = '\033[0m'

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.pattern = "{0[caller]}:{0[line]} - {0[string]}"
        self.last_log = dict()

    def setVerbose(self, verbose=False):
        "Set verbosity of Logger."
        self.verbose = verbose

    def setOutputPattern(self, pattern):
        """Sets the pattern to be used for output.
        For info, call getPatternTokens()."""
        self.pattern = pattern

    def log(self, s):
        "Log function, prints only if verbose is set"
        self.last_log = dict()
        import inspect
        stack = inspect.stack()
        self.last_log['caller'] = stack[1][3]
        self.last_log['line'] = stack[1][2]
        self.last_log['string'] = s
        if self.verbose:
            print(
                self.colour
                + self.pattern.format(self.last_log)
                + self.colourEnd
            )

    def getPatternTokens(self):
        "Returns the tokens that can be used in the pattern."

        if len(self.last_log.keys()) == 0:
            prevVerbose = self.verbose
            self.setVerbose(False)
            self.log('')
            self.setVerbose(prevVerbose)
        return self.last_log.keys()

    def setColour(self, colour):
        "Sets the colour of output."
        self.colour = colour

def round_to(n, precision):
    "Rounds to the nearest precision specified."
    correction = 0.5 if n >= 0 else -0.5
    return int(n/precision+correction)*precision


def mypath():
    "returns the script path"
    import os
    return os.path.dirname(os.path.realpath(__file__))
