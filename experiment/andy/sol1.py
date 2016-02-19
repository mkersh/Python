from sympy import *
n, fn = symbols("n fn")

expr = (5-77*sin(n)+8*n**2)/(1-4*n**2)
L = limit(expr,n,oo)
ep = (1.0/500)
print("Limit:", L)

expr2 = abs( fn - L )
expr2 = expr2.subs(fn, expr)

def seq(expr, a, b, evaluate=False):
    nlist = range(a,b+1)
    s = []
    if type(expr) == list:
        for i in nlist:
            s.append([i, expr[1].subs(n,i)])
    else:
        for i in nlist:
            if evaluate == False:
                s.append(expr.subs(n,i))
            else:
                s.append((expr.subs(n,i)).evalf())
    return s

# Work out lowest value m such that expr2 < ep for all n >= m
for i in range(44, 300): # if this doesn't generate an answer increase the size of the range
    s = seq(expr2,i,i+10,True) # generate the sequence for n = i .. i+10
    foundAnswer = True # this will be set False below if m=i is not the answer
    for seqVal in s:
        if seqVal >= ep:
            # NO one of the seqVal's is >= 1/500
            foundAnswer = False # This value of i is not the answer
            break # Move on to the next i
    if foundAnswer == True:
        # We have our foundAnswer
        print("Lowest m such that expr2 < ep for all n>=m is:", i)
        break # Break out of the outer for loop
    
# Plot a graph of the result from previous part
#import matplotlib
#matplotlib.use('Agg') # I need to do this to generate a file rather than onscreen
#import matplotlib.pyplot as plt

#nlist = list(range(100,131)) # has to be 131 becuaes of the def of seq func that add +1 to b
#print("length x", len(nlist))
#s = seq(expr2,100,130,True)
#print("length s", len(s))
#plt.plot(nlist, s)
#plt.savefig('diag.png')

plot(expr2, (n, 100, 131))