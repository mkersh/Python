def main():
	t1 = "This is a string"
	print(t1)
	t2 = list(t1)
	print(t2)
	n = 1024
	littleN = n % 63
	print(littleN)

	lst = ['A' for x in range(10) ]
	print("{0} len={1}".format(lst,len(lst)))
	print("{0} len={1}".format(str(lst),len(str(lst))))

	t4 = list("123")
	t5 = t4 + t4
	print(t5)

	t1 = "abcd"
	t2 = t1[0]
	t3 = t1[1:]
	print(t2)
	print(t3)
	
if __name__ == '__main__':	
	main()