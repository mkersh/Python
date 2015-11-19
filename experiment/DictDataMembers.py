import time

class STOPWATCH:
	clocks = {}

	def start(self, label='def'):
		t = time.time()
		# Store time in clocks dict, using label as key
		# Will have to store an object when start doing lap times but for now just the current time
		# will do		
		STOPWATCH.clocks[label] = t 

	def stop(self, label='def'):
		t = time.time()
		return t - STOPWATCH.clocks[label]

	def stopAndPrint(self, label='def'):
		t = self.stop(label)
		print("STOPWATCH Timing ({0}): {1} secs".format(label,t))


class DictClass:
	"""This class stores all its data members in a _privates dictionary.
	Access to a data member is via get() and set() methods
	"""
	_privates = {}

	def __init__(self):
		self.set("dataItem1", 12)
		self.set("dataItem2", "some String")
		self.set("dataItem3", [1,2,3,4,5,6,7])

	def get(self, it):
		return self._privates[it]

	def set(self, it, val):
		self._privates[it] = val

class OrdinaryClass:
	dataItem1 = 12
	dataItem2 = "some String"
	dataItem3 = [1,2,3,4,5,6,7]

	def get(self, it):
		return self[it]

	# This next method makes the class subscriptable. i.e. You can do obj["datamember"]
	def __getitem__(cls, x):
		return getattr(cls, x)

# Similar to OrdinaryClass but data members at object level rather than class level
class OrdinaryClass2:
	dataItem1 = 0
	dataItem2 = ""
	dataItem3 = []

	def __init__(self):
		self.dataItem1 = 12
		self.dataItem2 = "some String"
		self.dataItem3 = [1,2,3,4,5,6,7]

	def get(self, it):
		return self[it]

	# This next method makes the class subscriptable. i.e. You can do obj["datamember"]
	def __getitem__(cls, x):
		return getattr(cls, x)

def doSomething(str):
	pass
	#print(str)

def main():
	sw = STOPWATCH()
	obj1 = OrdinaryClass()
	#obj1 = OrdinaryClass2() # OrdinaryClass and OrdinaryClass2 are practically the same in terms of timings
	obj2 = DictClass()
	NUMBER_ITERS = 500000

	print("[1] Data member direct access")
	sw.start()
	for i in range(NUMBER_ITERS):
		doSomething("obj1 = ({0},{1},{2})".format(obj1.dataItem1, obj1.dataItem2, obj1.dataItem3))
	sw.stopAndPrint()

	print("[2] Data member subscriptable access")
	sw.start()
	for i in range(NUMBER_ITERS):
		doSomething("obj1 = ({0},{1},{2})".format(obj1["dataItem1"], obj1["dataItem2"], obj1["dataItem3"]))
	sw.stopAndPrint()

	print("[3] Data member generic get method")
	sw.start()
	for i in range(NUMBER_ITERS):
		doSomething("obj1 = ({0},{1},{2})".format(obj1.get("dataItem1"), obj1.get("dataItem2"), obj1.get("dataItem3")))
	sw.stopAndPrint()

	print("[4] Data members in _privates dictionary")
	sw.start()
	for i in range(NUMBER_ITERS):
		doSomething("obj2 = ({0},{1},{2})".format(obj2.get("dataItem1"), obj2.get("dataItem2"), obj2.get("dataItem3")))
	sw.stopAndPrint()
	

if __name__ == '__main__':
	main()