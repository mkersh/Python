import oata.HelloWorld
import pdb

# Inherit from the Java class that provides the SayHello() method
class MySubClass(oata.HelloWorld):
	def SayHelloAgain(self):
		print("and hello from me a python class that inherits from it")

def main():
	# enable the below if you need to debug
	#pdb.set_trace()
	c = MySubClass()
	fromJavaStr = c.SayHello()
	print(fromJavaStr)
	c.SayHelloAgain()

if __name__ == '__main__':
	main()