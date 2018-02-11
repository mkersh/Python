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
	# The next if statement is where all the magic happens. See [A] below
    if (n == len(set(vec[i]+i for i in cols))
          == len(set(vec[i]-i for i in cols))):
        print("[{0}] {1}").format(sol, vec)
        sol += 1 # extra line I added
SW.stopAndPrint()

# [A] The secret to solving the queens problem is having a way to determine if 2 queens
# are on the same diagonal. 
#
# Preventing them being on same row and column is easy and 
# with the approach above and the vector/collection data structure being used we ensure that
# they are never on same row or column.
#
# If queens are on the same diagonal then:
#     vec[i]+i for i in cols OR
#     vec[i]-i for i in cols
# will have one or more duplicate items.
# To really understand this draw a chess board grid. Number the rows and columns 
# and do the maths for a number of positions where queens are on the same diagonal.
# From this you'll see that the above is always true.
