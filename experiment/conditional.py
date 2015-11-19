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

def error(str):
	raise Exception(str)

def doWork(str):
	pass

def sparsify(d):
    """Improve dictionary sparsity.

    The dict.update() method makes space for non-overlapping keys.
    Giving it a dictionary with 100% overlap will build the same
    dictionary in the larger space.  The resulting dictionary will
    be no more that 1/3 full.  As a result, lookups require less
    than 1.5 probes on average.

    Example:
    >>> import __builtin__
    >>> sparsify(__builtin__.__dict__)

    """

    e = d.copy()
    d.update(e)

def conditionalTest(trigger):
	"""
	Python does NOT have a conditional statement but you can use a dictionary to achieve one.
	The alternative is to have a big long if .. elif statement.
	How do these dictionary versions of conditional statements perform though?
	That's what I am testing in this file
	"""
	actions = {
		'this': lambda: [
			doWork("this1"),
			doWork("this2"),
			doWork("this3")],
		'that': lambda: [
			doWork("that1"),
			doWork("that3"),
			doWork("that3")], 
		'why': lambda: [
			doWork("why1"),
			doWork("why2"),
			doWork("why3")],
		'how': lambda: [
			doWork("how1"),
			doWork("how2"),
			doWork("how3")], 
		'dummy1':  lambda: [],
		'dummy2':  lambda: [],
		'dummy3':  lambda: [],
		'dummy4':  lambda: [],
		'dummy5':  lambda: [],
		'dummy6':  lambda: [],
		'dummy7':  lambda: [],
		'dummy8':  lambda: [],
		'dummy9':  lambda: [],
		'dummy10':  lambda: [],
		'last': lambda: [
			doWork("last1"),
			doWork("last2"),
			doWork("last3")] 
	}

	try:
		actions[trigger]()
	except Exception as e:
		error("ERROR: trigger {0} unknown".format(trigger))
	
def conditionalTest2(trigger):
	"""
	Trying to improve readability of conditionalTest
	"""
	actions = {}
	# Below has got multiline lambda's by having body of lambda in list
	actions['this']  = lambda: [
		doWork("this1"), 
		doWork("this2"), 
		doWork("this3")]
	actions['that']  = lambda: [
		doWork("that1"),
		doWork("that2"),
		doWork("that3")]
	actions['why']   = lambda: [
		doWork("why1"),
		doWork("why2"),
		doWork("why3")]
	actions['how']   = lambda: [
		doWork("how1"), 
		doWork("how2"), 
		doWork("how3")] 
	actions['dummy1'] =  lambda: []
	actions['dummy2'] =  lambda: []
	actions['dummy3'] =  lambda: []
	actions['dummy4'] =  lambda: []
	actions['dummy5'] =  lambda: []
	actions['dummy6'] =  lambda: []
	actions['dummy7'] =  lambda: []
	actions['dummy8'] =  lambda: []
	actions['dummy9'] =  lambda: []
	actions['dummy10'] =  lambda: []
	actions['last'] = lambda: [
		doWork("last1"),
		doWork("last2"),
		doWork("last3")] 

	try:
		return actions[trigger]()
	except Exception as e:
		error("ERROR: trigger {0} unknown".format(trigger))

_conditionalTest3_actions = {
	'this': lambda: [
		doWork("this1"),
		doWork("this2"),
		doWork("this3")],
	'that': lambda: [
		doWork("that1"),
		doWork("that3"),
		doWork("that3")], 
	'why': lambda: [
		doWork("why1"),
		doWork("why2"),
		doWork("why3")],
	'how': lambda: [
		doWork("how1"),
		doWork("how2"),
		doWork("how3")], 
	'dummy1':  lambda: [],
	'dummy2':  lambda: [],
	'dummy3':  lambda: [],
	'dummy4':  lambda: [],
	'dummy5':  lambda: [],
	'dummy6':  lambda: [],
	'dummy7':  lambda: [],
	'dummy8':  lambda: [],
	'dummy9':  lambda: [],
	'dummy10':  lambda: [],
	'last': lambda: [
		doWork("last1"),
		doWork("last2"),
		doWork("last3")] 
}

#sparsify(_conditionalTest3_actions) # This doesn't seem to make any difference

def conditionalTest3(trigger):
	"""
	Define the actions table externally
	"""
	actions = _conditionalTest3_actions

	try:
		actions[trigger]()
	except Exception as e:
		error("ERROR: trigger {0} unknown".format(trigger))

def ifTest(trigger):
	if trigger == 'this':
		doWork("this1")
		doWork("this2")
		doWork("this3")
	elif trigger == 'that':
		doWork("that1")
		doWork("that3")
		doWork("that3") 
	elif trigger == 'why':
		doWork("why1")
		doWork("why2")
		doWork("why3")
	elif trigger == 'how':
		doWork("how1")
		doWork("how2")
		doWork("how3")
	elif trigger == 'dummy1':
		pass
	elif trigger == 'dummy2':
		pass
	elif trigger == 'dummy3':
		pass
	elif trigger == 'dummy4':
		pass
	elif trigger == 'dummy5':
		pass
	elif trigger == 'dummy6':
		pass
	elif trigger == 'dummy7':
		pass
	elif trigger == 'dummy8':
		pass
	elif trigger == 'dummy9':
		pass
	elif trigger == 'dummy10':
		pass
	elif trigger == 'last':
		doWork("last1"),
		doWork("last2"),
		doWork("last3")
	else:
		error("ERROR: trigger {0} unknown".format(trigger))

def main():
	sw = STOPWATCH()
	NUMBER_ITERS = 5000000
	trigger = 'last'

	print("[1] Conditional Test - " + trigger)
	sw.start()
	for i in range(NUMBER_ITERS):
		conditionalTest(trigger)
	sw.stopAndPrint()

	print("[2] Conditional Test2 - " + trigger)
	sw.start()
	for i in range(NUMBER_ITERS):
		conditionalTest2(trigger)
	sw.stopAndPrint()

	print("[3] IF Test - " + trigger)
	sw.start()
	for i in range(NUMBER_ITERS):
		ifTest(trigger)
	sw.stopAndPrint()

	print("[4] Conditional Test3 - " + trigger)
	sw.start()
	for i in range(NUMBER_ITERS):
		conditionalTest3(trigger)
	sw.stopAndPrint()
	

if __name__ == '__main__':
	main()