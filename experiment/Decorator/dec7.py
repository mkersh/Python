
"""
Not sure if this is useful??
Came across it in http://stackoverflow.com/questions/5929107/python-decorators-with-parameters

Partials just create a high-level function by supplying the value of one or more of the lower order functions
parameters.
"""

from functools import partial

def _pseudo_decor(fun, argument):
    def ret_fun(*args, **kwargs):
        #do stuff here, for eg.
        print("decorator arg is {0}".format(argument))
        return fun(*args, **kwargs)
    return ret_fun

real_decorator = partial(_pseudo_decor, argument=2)

@real_decorator
def foo(*args, **kwargs):
    print("Foo called")

def main():
	foo()
	
if __name__ == '__main__':
	main()