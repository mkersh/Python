import unittest

class TestStringMethods(unittest.TestCase):

  def setUp(self):
      print("Setup code run") # run for each test

  def tearDown(self):
      print("TearDown code run") # run for each test

  def test_upper2(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper2(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split2(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
  # normally you would run as part of a test runner but if you just want to exrecise the test in this file
  unittest.main()