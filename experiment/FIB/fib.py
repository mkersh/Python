import sys
import os
import time
if __name__ == '__main__':
    pathDir = "../../ProxyRecorder"
    sys.path.insert(0,pathDir)
import unittest
from logit import *
import pdb

import time

class STOPWATCH:
    clocks = {}

    def start(self, label='def'):
        t = time.time()
        # Store time in clocks dict, using label as key
        # Will have to store an object when start doing lap times but for now just the current time
        # will do
        STOPWATCH.clocks[label] = t

    def stop(self, label='def'):
        t = time.time()
        return t - STOPWATCH.clocks[label]

    def stopAndPrint(self, label='def'):
        t = self.stop(label)
        DEBUG("STOPWATCH Timing ({0}): {1} secs".format(label,t))



def fib(n):
    "This is a simple recursive definition of fib. Doesn't perform very will though"
    assert n > 0, "n must be > 0 "
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibi(n):
    a, b = (0,1)
    for i in range(1,n):
        a, b = (b,a+b)
    return a

def fib2(n, memory = {1:0,2:1}):
    "More efficient recursive definition with memoisation"
    assert n > 0, "n must be > 0 "
    if n not in memory:
        memory[n] = fib2(n-2) + fib2(n-1)
    return memory[n]

NO_ITERS = 35

class TestConfigMethods(unittest.TestCase):

    def printResult(self, funcName, i, r):
        msg = "{0}({1})={2}".format(funcName,i,r)
        print(msg)
        DEBUG(msg)

    def test_fib1(self):
        sw = STOPWATCH()
        sw.start("FIB1")
        for i in range(1,NO_ITERS):
            r = fib(i)
            self.printResult("fib",i,r)
        sw.stopAndPrint("FIB1")

    def test_fibi(self):
        sw = STOPWATCH()
        sw.start("FIBi")
        for i in range(1,NO_ITERS):
            r = fibi(i)
            self.printResult("fibi",i,r)
        sw.stopAndPrint("FIBi")

    def test_fib2(self):
        sw = STOPWATCH()
        sw.start("FIB2")
        for i in range(1,NO_ITERS):
            r = fib2(i)
            self.printResult("fib2",i,r)
        sw.stopAndPrint("FIB2")

if __name__ == '__main__':
    unittest.main()
    print(p)