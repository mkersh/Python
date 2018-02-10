import sys
if __name__ == '__main__':
    pathDir = "../../utils"
    sys.path.insert(0,pathDir)
from stopwatch import *

num = 1
def nqueens(r,n,p):
  # p represents a potential board position for the queens. It is a vector that represents the column positions of queens for
  # a board with (eventually) n rows and n columns. The values in the vector identify column positions for the different rows.
  # With this algorithm p is built up gradually.
  # So we start with an empty vector (i.e. no columns allocated) and then we add to it below.
  global num
  s  = len(p)
  cols = range(s)
  # This next line is performing the diagonal check on p to see if it is valid so far
  valid = s == len(set(p[i] + i for i in cols)) == len(set(p[i] - i for i in cols))

  count = 0

  if valid:
    if r == n:
      print("[{i}] {vec}").format(i=num,vec=p)
      num += 1
      return 1
    # This next line is performing all the magic. It is doing a set difference and only considering columns not currently considered  
    # We then call nqueens recursively. This will check that the item we have just added is valid
    # If valid then number of items in p == n then we have found a solution else we add more items
    for c in set(range(n)) - set(p):
        count += nqueens(r + 1, n, p + [c])

  return count


def backtracknqueens(n):
    print n, nqueens(0,n,[])

if __name__ == '__main__':
  SW = STOPWATCH()
  SW.start()
  backtracknqueens(8)
  SW.stopAndPrint()