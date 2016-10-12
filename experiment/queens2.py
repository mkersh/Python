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
  backtracknqueens(8)