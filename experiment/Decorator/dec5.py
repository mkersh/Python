
"""
passing parameters to the decorator.
"""


# This looks confusing at first but when you think about it it makes sense
# A decorator is a callable that takes a function to modify.
# If you want to pass parameters to the decorator then you need an outer closure function
def decorator(argument):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            print('PRE stuff')
            function(argument, *args, **kwargs)
            print('POST stuff')
        return wrapper
    return real_decorator


@decorator(1) # decorator(1) evaluates to the real_decorator function but the argument=1 is captured in a closure and available 
def sayHello1(id):
	"sayHello1 doc string"
	print("Hello: {0}".format(id))

@decorator(2)
def sayHello2(id):
	"sayHello2 doc string"
	print("Hello22: {0}".format(id))


def main():
	sayHello1()
	sayHello2()
	
if __name__ == '__main__':
	main()