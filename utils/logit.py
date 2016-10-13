"""
Provides a simple facade over the standard python logging
"""
import sys, traceback
import os
import time
import datetime
import logging
import logging
import logging.handlers
try:
    from StringIO import StringIO
except ImportError:
    # Python 3.x
    from io import StringIO

LOG_FILENAME = 'logs/debug.txt'
my_logger = None
_CURR_FUNC = None

def DEBUG(msg,logger=None):
    global _CURR_FUNC
    cf = _currentFunction(1)
    if cf != _CURR_FUNC:
        _CURR_FUNC = cf
        my_logger.debug("In Function: {0}----------------".format(cf))
    my_logger2.debug(msg)

def INFO(msg,logger=None):
    my_logger.info(msg)

def WARN(msg,logger=None):
    my_logger.warning(msg)

def ERROR(msg,logger=None):
    my_logger.error(msg)


def LOGFILE():
    return os.path.abspath(LOG_FILENAME)

def _getLastFunc(framePos = 0, numFrames = 1):
    """Get the last function prior to the logging calls"""
    assert numFrames > 0, "Invalid numFrames = {0}".format(numFrames)
    stackList = traceback.extract_stack()
    l = len(stackList)
    stIndex = l-3-framePos
    if stIndex < 0:
        assert False, "Stackframe {0} not available".format(framePos)
    else:
        i = stIndex
        while i > -1:
            stFrame = stackList[i]
            i = i - 1
            yield stFrame
            numFrames = numFrames - 1
            if numFrames == 0:
                break
        return

def _currentFunction(framePos = 0):
    return list(_getLastFunc(framePos))[0][2]

def STACKTRACE(framePos = 0, numFrames = 1):
    output = StringIO()
    output.write("Stack Dump (most recent first):\n")
    i = framePos
    for fr in _getLastFunc(framePos, numFrames):
        output.write("\t[{0}] - {1}\n".format(i,fr))
        i += 1
    DEBUG(output.getvalue())
    output.close()

def _secondsSinceMidnight():
    today = datetime.date.today()
    seconds_since_midnight = time.time() - time.mktime(today.timetuple())
    return seconds_since_midnight

class ContextFilter(logging.Filter):
    """
    This is a filter which injects seconds since midnight into the log.
    """
    def filter(self, record):
        record.SECS = _secondsSinceMidnight()
        return True

def getLoggerClearLog():
    global LOG_FILENAME, my_logger, my_logger2

    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # Next formatter needs the ContextFilter to insert the SECS attribute
    #formatter = logging.Formatter('%(SECS)s - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(relativeCreated)d - %(name)s - %(levelname)s - %(message)s')

    handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=50000, backupCount=5)
    handler.setFormatter(formatter)
    handler.doRollover() # Force a new log
    my_logger.addHandler(handler)

    # Create a seperate my_logger2 that has a different formatter
    # Difference is that it indents the output by a TAB
    formatter2 = logging.Formatter('\t%(relativeCreated)d - %(name)s - %(levelname)s - %(message)s')
    handler2 = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=50000, backupCount=5)
    handler2.setFormatter(formatter2)
    my_logger2.addHandler(handler2)
    # Below filter needed if using SECS in formetter
    #my_logger.addFilter(ContextFilter())


def setLogLevel(iLevel):
    levels = {
        "ERROR": logging.ERROR,
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARN": logging.WARN
    }

    logLevel = levels[iLevel]
    my_logger.setLevel(logLevel)
    my_logger2.setLevel(logLevel)

def initLogger():
    global LOG_FILENAME, my_logger, my_logger2
    # Set up a specific logger with our desired output level
    my_logger = logging.getLogger('MyLogger')
    my_logger.setLevel(logging.DEBUG)
    my_logger2 = logging.getLogger('MyLogger2')
    my_logger2.setLevel(logging.DEBUG)
    #my_logger.setLevel(logging.INFO)
    #my_logger.setLevel(logging.WARN)
    #my_logger.setLevel(logging.ERROR)

    logsDir = os.path.dirname(LOG_FILENAME)
    if not os.path.exists(logsDir):
        os.makedirs(logsDir)

    getLoggerClearLog()


initLogger()

