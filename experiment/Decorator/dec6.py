
"""
nested decorators.
"""

def decorator1(function):
    def wrapper(*args, **kwargs):
        print('PRE dec1')
        function(*args, **kwargs)
        print('POST dec1')
    return wrapper

def decorator2(function):
    def wrapper(*args, **kwargs):
        print('PRE dec2')
        function(*args, **kwargs)
        print('POST dec2')
    return wrapper

def decorator3(function):
    def wrapper(*args, **kwargs):
        print('PRE dec3')
        function(*args, **kwargs)
        print('POST dec3')
    return wrapper

@decorator1
@decorator2
@decorator3
def sayHello1():
	"sayHello1 doc string"
	print("Hello 111")

def main():
	sayHello1()
	
if __name__ == '__main__':
	main()