from math import * # Andy you probably don't need this line in your environment.

n = 0

while (abs(((5-77*sin(n)+8*(n**2))/(1-4*(n**2)))+2) > (1/500)):
	print('trying n is:', n)
	n = n + 1

print("Answer:", n)