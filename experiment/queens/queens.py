import sys
if __name__ == '__main__':
    pathDir = "../../utils"
    sys.path.insert(0,pathDir)
from stopwatch import *
from itertools import permutations

SW = STOPWATCH()
SW.start()
sol = 1 # extra line I added
n = 10
cols = range(n)

for vec in permutations(cols):
    if (n == len(set(vec[i]+i for i in cols))
          == len(set(vec[i]-i for i in cols))):
        print("[{0}] {1}").format(sol, vec)
        sol += 1 # extra line I added
SW.stopAndPrint()
