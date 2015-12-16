import unittest
import pdb

def discoverRunTest(pathToSearch):
    """
    Search and run tests found in pathToSearch.
    NOTE: This search is not recursive, only looks in the folder pointed to by pathToSearch
    """
    testsuite = unittest.TestLoader().discover(pathToSearch)
    unittest.TextTestRunner(verbosity=2).run(testsuite)

if __name__ == '__main__':
    #pdb.set_trace()
    discoverRunTest("tests")
    # You can run multiple runners if required
    #discoverRunTest("tests2")
	