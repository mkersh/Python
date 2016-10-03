import sys
if __name__ == '__main__':
    sys.path.insert(0,"..")
import unittest
from logit import *
import pdb

class TestConfigMethods(unittest.TestCase):

    def test_LogMethods(self):
      DEBUG("Debug msg1")
      DEBUG("Debug msg2")
      DEBUG("Debug msg3")
      INFO("Info msg2")
      WARN("Warn msg3")
      ERROR("Error msg4")
      STACKTRACE(numFrames = 999)
    def test_LogMethods2222(self):
      DEBUG("Debug msg4")
      DEBUG("Debug msg5")
if __name__ == '__main__':
    unittest.main()