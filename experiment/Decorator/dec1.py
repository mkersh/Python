import types

def decorator(func_todecorate):
	""" Decorate the function passed in. Returning a new function"""
	if type(func_todecorate) != types.FunctionType:
		print("You can only decorate functions")
	def func_to_return ():
		print("Pre function call decoration")
		func_todecorate()
		print("Post function call decoration")
	return func_to_return

def sayHello():
	print("Hello there")

def main():
	print("Without decorator")
	sayHello()
	print("With decorator")
	decorator(sayHello)()
	# Now Let's replace original definition
	sayHello2 = decorator(sayHello) # Original thought you could do sayHello = decorator(sayHello) but you cant
	#sayHello = sayHello2 # This is not allowed either because line 18 then fails. The original function is no longer visible
	print("After moded original function with permanent decoration")
	sayHello2()
	
if __name__ == '__main__':
	main()