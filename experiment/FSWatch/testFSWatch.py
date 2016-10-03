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

    def test_CanAccessCommonModule(self):
        abPath = os.path.abspath(pathDir)
        logFile = LOGFILE()
        print(abPath)
        print(logFile)
        self.assertTrue(os.path.exists(abPath))
        self.assertTrue(os.path.exists(logFile))
        DEBUG("Accessing from logit")

    def test_DirectoryModTime(self):
        dir1 = "testDir"
        fn = "testDir/f4"
        #touch(fn)
        # Was hoping that parent dir would get its mod date updated every time there was a change
        # to any file in the dir but this is not the case.
        # The dir modTime only gets updated if a new file is added
        DEBUG( time.ctime(os.path.getmtime(dir1)))

    def test_DirectoryModRecursive(self):
        dir1 = "testDir"
        fswatch.getFileModList(10, dir1)
        lmTime = fswatch.getLastModTime(dir1)
        DEBUG(lmTime)
        print(lmTime)

    def test_bigSearch(self):
        dir1 = "c:\\Program Files"
        #dir1 = "c:\\"
        fswatch.getFileModList(10, dir1)
        #lmTime = fswatch.getLastModTime(dir1)
        #DEBUG(lmTime)
        #print(lmTime)

if __name__ == '__main__':
    unittest.main()
    print(p)