import sys
from itertools import permutations
if __name__ == '__main__':
    pathDir = "../../utils"
    sys.path.insert(0,pathDir)
from permute import *
from stopwatch import *

def queensDiagonalCheckValid(perm):
    n = len(perm) 
    if n < 2:
        return True
    cols = range(n)
    res = (n == len(set(perm[i]+i for i in cols)) == len(set(perm[i]-i for i in cols)))
    return res

SW = STOPWATCH()
SW.start()
sol = 1 
n = 14
cols = range(n)

for vec in permutate(cols, queensDiagonalCheckValid):
    print("[{0}] {1}").format(sol, vec)
    sol += 1 

SW.stopAndPrint()