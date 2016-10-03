import sys
import os
import time
if __name__ == '__main__':
    pathDir = "../../ProxyRecorder"
    sys.path.insert(0,pathDir)
import unittest
from logit import *
import fswatch

def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)

class TestConfigMethods(unittest.TestCase):

    def test_bigSearch(self):
        #dir1 = "c:\\Program Files"
        dir1 = "c:\\"
        fswatch.getFileModList(10, dir1)
        #lmTime = fswatch.getLastModTime(dir1)
        #DEBUG(lmTime)
        #print(lmTime)

if __name__ == '__main__':
    unittest.main()
    print(p)