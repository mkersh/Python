# This file is intended for trying out python examples quickly
from math import pi
list = ["one", "two", 676.90]

#del list[1]
print(list[::-1]) # print in reverse

for i,val in enumerate(list):
    print(i,val)

str2="Hello World this is Mark!!"


print(str2,str2[::-1])

print(str(pi)[0:100])

def f1():
    i = 0
    while True:
        yield i
        i += 1

for i in f1():
    print("==>", i)
    if i > 100:
        break

