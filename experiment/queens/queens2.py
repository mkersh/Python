import sys
if __name__ == '__main__':
    pathDir = "../../utils"
    sys.path.insert(0,pathDir)
from stopwatch import *

num = 1
def nqueens(r,n,p):
  # p represents a potential board position for the queens. It is a vector that represents the column positions of queens for
  # a board with n rows and n columns. The values in the vector identify column positions for the different rows.
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