
# This is an alternative to import aota.HelloWorld which you then have to fully qualify class 
# whenever you use
from oata import HelloWorld2
import pdb

# Inherit from the Java class that provides the SayHello() method
class MySubClass(HelloWorld2):
	# Override the HelloWorld SayHello method
	def SayHello(self):
		return "Hello from python"
	def SayHelloAgain(self):
		print("SayHelloAgain")

def main():
	# enable the below if you need to debug
	#pdb.set_trace()
	c = MySubClass()
	fromJavaStr = c.SayHello()
	print(fromJavaStr)
	c.SayHelloAgain()
	# This next call is the interesting one because it proves that SayHello has really overridden SayHello in the BaseClass
	# because doit() is in the base class and will call out to SayHello()
	c.doit()

	# See if it can handle multiple methods with same method name different signature
	#c.SayHello(1)
	#c.SayHello(1,"me")
	
	# Next two pick up the correct base class method
	HelloWorld2.SayHello(c, 1)
	HelloWorld2.SayHello(c, 1, "This is it")

	# NOTE: If the method is protected then you can't call from the class directly you have to use
	c.super__SayHello(1, "This is it")

if __name__ == '__main__':
	main()