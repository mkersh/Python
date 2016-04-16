from math import exp
from sympy import *
import sys
#import matplotlib

x = symbols("x")

expr = ((x/2)*exp(0.5 - 0.5*x*x))
vel = diff(expr)
acc = diff(vel)


#print("[1 Part]----------------------")
#plot(expr, (x, -4, 4))

#print("[2 Part]-----------------------")

plot(expr, (x, -4, 4))
plot(vel, (x, -4, 4))
plot(acc, (x, -4, 4))
