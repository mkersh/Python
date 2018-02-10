import sys
from itertools import permutations
if __name__ == '__main__':
    pathDir = "../../utils"
    sys.path.insert(0,pathDir)
from permute import *
from stopwatch import *

# This approach for working out the nXn queens problems uses the same
# algorithm as queens.py but is using my own implementation of permutate
SW = STOPWATCH()
SW.start()
sol = 1 # extra line I added
n = 10
cols = range(n)

for vec in permutate(cols):
    if (n == len(set(vec[i]+i for i in cols))
          == len(set(vec[i]-i for i in cols))):
        print("[{0}] {1}").format(sol, vec)
        sol += 1 # extra line I added

SW.stopAndPrint()