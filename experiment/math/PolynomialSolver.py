from sympy import *
y, x, z = symbols("y x z")

expr  = y=(x**2)+(3*x)+2
expr2 = y=(x**3)+(2*x**2)+(3*x)+2

pprint(expr) # Pretty print expression
print(solve(expr, x))

