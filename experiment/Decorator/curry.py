
import inspect

class curried(object):
  '''
  Decorator that returns a function that keeps returning functions
  until all arguments are supplied; then the original function is
  evaluated.

  MK: Is there a practical use for this? I'm sure there is but I don't know of one

  Currying -> https://en.wikipedia.org/wiki/Currying
  '''

  def __init__(self, func, *a):
    self.func = func
    self.args = a
    # func_code.co_argcount only works in python2
    # need a way to determine number of positional arguments expected
    # See http://stackoverflow.com/questions/990016/how-to-find-out-the-arity-of-a-method-in-python
    # next line return a tuple with 4 items args, varargs, varkw, defaults
    # It works on both Python 2 and 3
    self.funcArgsSpec = inspect.getargspec(func) 
    self.NumParams = len(self.funcArgsSpec[0])

  def __call__(self, *a):
    args = self.args + a
    # Original code had the following but it only works on python 2
    #if len(args) < self.func.func_code.co_argcount:
    if len(args) < self.NumParams:
      return curried(self.func, *args)
    else:
      return self.func(*args)


@curried
def add(a, b):
    return a + b

@curried
def add3(a, b, c):
    return a + b + c



def main():
	add1 = add(1)
	print(add1(2))
	print(add3(10)(13)(15))
	print(add3(10,13,15))
	print(add3(10,13)(15))
	
if __name__ == '__main__':
	main()