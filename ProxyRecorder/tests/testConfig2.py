import sys
if __name__ == '__main__':
    sys.path.insert(0,"..")
import unittest
import configFile as c

class TestConfigMethods(unittest.TestCase):

  def test_AbsoluteConfigPath(self):
      con = c.Config(r"C:\cygwin64\home\mkershaw\python\ProxyRecorder\tests\config\Config2.txt")
      recObject = con.getRecordingSetting("RecordingName")
      self.assertEqual(recObject["name"], "RecordingName")
      self.assertEqual(recObject["webservice-type"], "SOAP")

  def test_RelativeConfigPath(self):
      con = c.Config(r"tests\config\Config2.txt")
      recObject = con.getRecordingSetting("RecordingName")
      self.assertEqual(recObject["name"], "RecordingName")
      self.assertEqual(recObject["webservice-type"], "SOAP")

if __name__ == '__main__':
    unittest.main()