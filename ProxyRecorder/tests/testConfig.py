import sys
if __name__ == '__main__':
    sys.path.insert(0,"..")
import unittest
import configFile as c

class TestConfigMethods(unittest.TestCase):

  def test_RecordingSettings(self):
      con = c.Config()
      recObject = con.getRecordingSetting("RecordingName")
      self.assertEqual(recObject["name"], "RecordingName")
      self.assertEqual(recObject["webservice-type"], "SOAP")
      self.assertEqual(len(recObject["messages"]), 3)
      msg = recObject["messages"][0]
      self.assertEqual(msg["name"], "msg1")
      self.assertEqual(msg["match.url.1"], "RegExUrl1")
      self.assertEqual(msg["match.url.2"], "RegExUrl2")
      self.assertEqual(msg["match.body.1"], "RegExBody1")
      self.assertEqual(msg["match.body.2"], "RegExBody2")
      msg = recObject["messages"][1]
      self.assertEqual(msg["name"], "msg2")
      msg = recObject["messages"][2]
      self.assertEqual(msg["name"], "msg3")

if __name__ == '__main__':
    unittest.main()