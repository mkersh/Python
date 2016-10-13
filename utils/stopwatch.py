
import time
from logit import *

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
		INFO("STOPWATCH Timing ({0}): {1} secs".format(label,t))
