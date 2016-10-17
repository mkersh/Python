import sys
if __name__ == '__main__':
    pathDir = "../../utils"
    sys.path.insert(0,pathDir)
from stopwatch import *

num = 1
def nqueens(r,n,p):
  global num
  s  = len(p)
  cols = range(s)
  valid = s == len(set(p[i] + i for i in cols)) == len(set(p[i] - i for i in cols))

  count = 0

  if valid:
    if r == n:
      print("[{i}] {vec}").format(i=num,vec=p)
      num += 1
      return 1

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