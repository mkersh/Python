# http://stackoverflow.com/questions/21196814/prime-numbers-and-factorials

def pf(number):
    factors=[]
    d=2
    while(number>1):
        while(number%d==0):
            factors.append(d)
            number=number/d
        d+=1
    return factors

def pf2(number):
    factors=set()
    d=2
    while(number>1):
        while(number%d==0):
            factors.add(d)
            number=number/d
        d+=1
    return factors

def main():
	print(pf(1000000))

if __name__ == '__main__':
	main()