

class DoWork():
	_Counter = 0 # Class level member

	@classmethod
	def incClassCounter(cls):
	    c = cls._Counter
	    c += 1
	    cls._Counter = c

	def sayHello(self):
		self.incClassCounter()
		print("Hello I am DoWork {0}".format(self._Counter))

def main():
	dw = DoWork()
	dw.sayHello()
	dw.sayHello()
	dw2 = DoWork()
	dw2.sayHello()
	dw2.sayHello()

if __name__ == '__main__':
	main()