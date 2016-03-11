import sys
"""
Explicitly extending the sys.path.
Not the most elegant way to do it but it works.
I suspect there is a better way though using packages and sub-packages
and that is what I am experimenting in LogicGateModTest.
"""
def addPath(path):
    if str(sys.path).find(path) == -1:
        sys.path.insert(0,path)
addPath("../simulator")
addPath("../circuits")
from explicit_c1 import *


if __name__ == '__main__':
    main() # This calls explicit_c1.main