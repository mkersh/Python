import sys
import pdb
if __name__ == '__main__':
    sys.path.insert(0,"..")
import unittest
from recorder import Recorder

class TestRecorder1(unittest.TestCase):

    def test_SocketPair1(self):
        rec = Recorder()
        rec.createSocketPair(1,2)
        socDetails = rec._getSocketDetails(1)
        self.assertEqual(socDetails["socketPair"], 2)
        self.assertEqual(socDetails["isForwardChannel"], False)
        socDetails = rec._getSocketDetails(2)
        self.assertEqual(socDetails["socketPair"], 1)
        self.assertEqual(socDetails["isForwardChannel"], True)

    def test_SocketPair2(self):
        rec = Recorder()
        rec.createSocketPair(1,2)
        self.assertTrue(rec.isForwardSocket(2))
        self.assertFalse(rec.isForwardSocket(1))
        self.assertEqual(rec.getSocketPair(2),1)
        self.assertEqual(rec.getSocketPair(1),2)
        rec.createSocketPair(3,4)
        self.assertTrue(rec.isForwardSocket(4))
        self.assertFalse(rec.isForwardSocket(3))
        self.assertEqual(rec.getSocketPair(4),3)
        self.assertEqual(rec.getSocketPair(3),4)

    def test_SocketPairClose(self):
        rec = Recorder()
        rec.createSocketPair(1,2)
        self.assertTrue(rec.isForwardSocket(2))
        self.assertFalse(rec.isForwardSocket(1))
        self.assertEqual(rec.getSocketPair(2),1)
        self.assertEqual(rec.getSocketPair(1),2)
        self.assertEqual(rec.socketCount(),2)
        rec.closeSocket(1)
        with self.assertRaises(Exception) as context:
           self.assertTrue(rec.isForwardSocket(2))
        self.assertEqual(rec.socketCount(),0)

    def test_SocketData1(self):
        rec = Recorder()
        rec.createSocketPair(1,2)
        self.assertEqual(rec.getSocketData(1), None)
        self.assertEqual(rec.getSocketData(2), None)

    def test_RecordMessage(self):
        rec = Recorder()
        rec.createSocketPair(1,2)
        rec.recordMessage(1,"Hello World")
        self.assertEqual(rec.getSocketData(1), "Hello World")
        rec.recordMessage(1,"xxx")
        self.assertEqual(rec.getSocketData(1), "Hello Worldxxx")
        rec.recordMessage(2,"1")
        rec.recordMessage(2,"2")
        rec.recordMessage(2,"3")
        self.assertEqual(rec.getSocketData(2), "123")

    def test_RecorderConfig(self):
        rec = Recorder()
        recObject = rec.getConfig().getRecordingSetting("RecordingName")
        self.assertEqual(recObject["name"], "RecordingName")

    def test_SocketPairMissing1(self):
        rec = Recorder()
        rec.createSocketPair(1,2)
        with self.assertRaises(Exception) as context:
            socDetails = rec._getSocketDetails(3)

    def test_SocketPairMissing2(self):
        rec = Recorder()
        with self.assertRaises(Exception) as context:
            socDetails = rec._getSocketDetails(1)



if __name__ == '__main__':
    unittest.main()