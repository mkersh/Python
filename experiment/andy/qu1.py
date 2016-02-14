import math

ansFound = False

# Define the function a as a python function
def f(n):
	sn = math.sin(n)
	a = (5 -(77*sn) + 8*n*n)/(1 - (4*n*n))
	return a

L = -2   # Defines the Limit that you found in part i
ep = (1/500)

for i in range(1000):
	if (abs(f(i) - L)) < ep:
		print("Answer is {0}".format(i)) 
		ansFound = True
		break 

if ansFound == False:
	print("Did not find an answer")

