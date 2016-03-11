import sys
"""
If you want to potentially run this module explicitly then you need to make sure all
sub-folders are on path.
NOTE: If you call from explicit_t1.py then you don't need the addPath stuff, because
the folders will already be on your sys.path
"""
def addPath(path):
    """
    Reason I am using addPath rather than just inserting directly onto sys.path is to
    prevent duplicate directories being added to the path
    """
    if str(sys.path).find(path) == -1:
        sys.path.insert(0,path)
addPath("../simulator")
#addPath("../circuits") # Don't need this because . is already on path
from sim import *
import explicit_c2 as c2

def makeCircuit():
    print("explicit_c1 make Circuit")
    simulator("from explicit_c1")
    c2.makeCircuit()
def main():
    print("explicit_c1 main called")
    makeCircuit()
if __name__ == '__main__':
    main()