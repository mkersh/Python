#precision = 0.00000000001
precision = 0.00000001

def sqrt(x):
	return sqrt_iter(1,x)

def sqrt_iter(guess, x):
	if good_enough(guess, x):
		return guess
	else:
		return sqrt_iter(improve_guess(guess,x), x)

def good_enough(guess, x):
	return abs((guess*guess) - x) < precision

def improve_guess(guess,x):
	return average( guess, x / float(guess))

def average(x,y):
	return (x + y)/2 

#print 5 / float(2)

for x in range(10):
	print "SQRT({0})={1}".format(x,sqrt(x))
#print sqrt(9)
#print sqrt(25)
#print sqrt(2)
#print sqrt(144)
