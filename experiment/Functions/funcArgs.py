"""
Experiments into how python function arguments work
"""

def func1(pos1, pos2, pos3):
	"""
	This function takes 3 mandatory positional arguments.
	If you call without all 3 you will get an error
	"""
	print("func1 called with {0} {1} {2}".format(pos1, pos2, pos3))

def func2(pos1="a", pos2="b", pos3="c"):
	"""
	This function takes 3 positional arguments with defaults
	"""
	print("func2 called with {0} {1} {2}".format(pos1, pos2, pos3))

def func3(pos1, *argv):
	"""
	This function takes 1 mandatory positional argument and an argv list of others.
	As many others as you want can be passed
	"""
	print("func3 called with {0} {1}".format(pos1, argv))

def apply(func, *argv):
	"""
	Indirect way to call a function that makes it easier to test negative cases
	"""
	try:
		func(*argv)
	except Exception as e:
		print("Function call failed {0}".format(e))

def apply2(func, **kargv):
	"""
	Indirect way to call a function that makes it easier to test negative cases
	"""
	try:
		func(**kargv)
	except Exception as e:
		print("Function call failed {0}".format(e))

def apply3(func, *argv, **kargv):
	"""
	Indirect way to call a function that makes it easier to test negative cases.

	Args:

	*argv: Will match any positional arguments passed
	**kargv: Will match any keyword arguments passed
	"""
	try:
		func(*argv, **kargv)
	except Exception as e:
		print("Function call failed {0}".format(e))
	

def main():
	func1(1,2,3)
	apply(func1, 1, 2, 3)
	apply(func1, 1,2) # Will fail with missing positional argument
	apply(func1, 1,2,3,4) # passing too many parameters will not fail in python

	func2(1,2,3)
	func2() # use default arguments

	# See if we can pass named parameters to func1
	print("Test is we can pass named parameters to func1")
	func1(pos1='x', pos2='y', pos3='z')
	func1(pos3='z', pos2='y', pos1='x')
	# apply() will not work if passing keyword arguments you have to use apply 2 instead
	apply2(func1,pos3='z', pos2='y', pos1='x')
	apply2(func1, pos3='z', pos2='y')

	apply3(func1, 7, pos3='z', pos2='y')

	# keyword arguments have to be after non-keyword arguments
	# The following would generate a syntax error
	#apply3(func1, 7, pos3='z', 8)
	

if __name__ == '__main__':
	main()