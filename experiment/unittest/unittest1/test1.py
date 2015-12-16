import unittest
import testOtherModule
import pdb

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

def discoverRunTest(pathToSearch):
  """
  Search and run tests found in pathToSearch.
  NOTE: This search is not recursive, only looks in the folder pointed to by pathToSearch
  """
  testsuite = unittest.TestLoader().discover('.')
  unittest.TextTestRunner(verbosity=2).run(testsuite)

if __name__ == '__main__':
  # When you call main it just picks up the tests in this file
	#unittest.main()
  # Setting up a TestLoader and getting it to auto discover is better
  # but it is not recursive
  
  pdb.set_trace()
  discoverRunTest(".")
  discoverRunTest("testDir")
	