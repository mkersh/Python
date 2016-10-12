from itertools import permutations
sol = 1 # extra line I added
n = 8
cols = range(n)
print(cols)
for vec in permutations(cols):
    if (n == len(set(vec[i]+i for i in cols))
          == len(set(vec[i]-i for i in cols))):
        print("[{0}] {1}").format(sol, vec)
        sol += 1 # extra line I added
    else:
    	#print("NOT SOLUTION -  {0}").format(vec)
    	pass
