import sys
import pdb
from itertools import permutations
import pdb
if __name__ == '__main__':
    pathDir = "../../utils"
    sys.path.insert(0,pathDir)
from logit import *
from stopwatch import *

SW = STOPWATCH()


def main():
    SW.start()
    #pdb.set_trace()
    n = 8
    cols = range(n)
    lst = [1,2,3,4]
    res = list(permutations(cols))
    print(len(res))
    #print(res)
    SW.stopAndPrint()

if __name__ == '__main__':
    main()
