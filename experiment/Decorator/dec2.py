import types

"""This next function decorates functions that take zero arguments"""
def decorator(func_todecorate):
	def func_to_return ():
		print("Pre function call decoration")
		func_todecorate()
		print("Post function call decoration")
	return func_to_return

"""This next decorator decorates functions that take two argguments"""
def decorator2Args(func_todecorate):
	def func_to_return (arg1, arg2):
		print("Pre function call decoration")
		func_todecorate(arg1,arg2)
		print("Post function call decoration")
	return func_to_return

def decoratorVarArgs(func_todecorate):
	def func_to_return (*args):
		print("Pre function call decoration")
		func_todecorate(*args) # Need to use * to expand parameters
		print("Post function call decoration")
	return func_to_return


def decoratorKVarArgs(func_todecorate):
	def func_to_return (**kargs):
		print("Pre function call decoration")
		func_todecorate(**kargs) # Need to use * to expand parameters
		print("Post function call decoration")
	return func_to_return

@decorator
def sayHello():
	print("Hello there")

@decorator2Args
def sayHello2(arg1, arg2):
	print("Hello222 there I was passed {0} {1}".format(arg1,arg2))

@decoratorVarArgs
def sayHello3(*args):
	print("Hello333 there I was passed {0} {1}".format(args[0],args[1]))


@decoratorVarArgs
def sayHello4(*args):
	print("Hello444 there I was passed {0} {1} {2}".format(args[0],args[1],args[2]))

@decoratorKVarArgs
def sayHello5(**kargs):
	print("Hello555 was passed {0} {1}".format(kargs['arg1'],kargs['arg2']))

def main():
	sayHello()
	sayHello2(1,2)
	sayHello3(1,2)
	args = [7,8]
	sayHello3(*args)
	sayHello4(4.1,4.2,4.3)
	sayHello5(arg1='This', arg2='that')
	dict = {'arg1':'why','arg2':'where'}
	sayHello5(**dict)
	
if __name__ == '__main__':
	main()