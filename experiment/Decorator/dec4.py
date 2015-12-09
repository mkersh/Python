
"""
This test looks at using functools wraps method.

This is the correct way to decorate a functions because it preserves attributes of the original functions
like __name__ and __doc__ string.

"""
from functools import wraps

def decoratorWithoutWraps(func_todecorate):
	def func_to_return ():
		print("Pre without")
		func_todecorate()
		print("Post without")
	return func_to_return

def decoratorWithWraps(func_todecorate):
	@wraps(func_todecorate)
	def func_to_return ():
		print("Pre with")
		func_todecorate()
		print("Post with")
	return func_to_return
	

@decoratorWithoutWraps
def sayHello1():
	"sayHello1 doc string"
	print("Hello there 111: {0} {1}".format(sayHello1.__name__,sayHello1.__doc__))

@decoratorWithWraps
def sayHello2():
	"sayHello2 doc string"
	print("Hello there 222: {0} {1}".format(sayHello2.__name__,sayHello2.__doc__))

def main():
	sayHello1()
	sayHello2()
	
if __name__ == '__main__':
	main()