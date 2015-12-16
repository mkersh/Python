import unittest
class TestMk2Methods(unittest.TestCase):

  def test_mk1(self):
      self.assertEqual('foo'.upper(), 'FOOf')

  def test_mk2(self):
      self.assertEqual('foo'.upper(), 'FOOd')
