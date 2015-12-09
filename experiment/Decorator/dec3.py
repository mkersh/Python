"""This test shows classed based decorators"""

class MyDecorator():
	def __init__(self, f):
		self.f = f
	def __call__(self, *args, **kwargs):
		print("Entering", self.f.__name__)
		self.f(*args, **kwargs)
		print("Exited", self.f.__name__)
		 
@MyDecorator
def func1():
	print("inside func1()")

@MyDecorator
def func2():
	print("inside func2()")

def func3():
	print("inside func3()")


def main():
	func1()
	func2()

	obj = MyDecorator(func3)

	obj() ## when no function name specified it will call __call__

	# can we make a callable dict. Answer is no.
	dict = {'arg1':1, '__call__': lambda: [print("calling the dictionary")]}
	#dict() # This doesn't eotk
	
if __name__ == '__main__':
	main()