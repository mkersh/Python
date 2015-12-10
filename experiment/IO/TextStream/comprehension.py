
def test1():
	nextVal = [-1]
	def testAndModify(x):
		print("{0} {1}".format(x, nextVal))
		x = 33 if x ==3 else x
		#nextVal = x*x # This doesn't work because nextVal is now local in this method
		nextVal[0] = x*x
		return True

	lst = [nextVal[0] for x in [1,2,3,4] if testAndModify(x)]
	print(lst)

nextVal = 0
def test2():
	def testAndModify(x):
		global nextVal # It does have to be a global though. If you declare nextVal in test2() it doesn't work
		print("{0} {1}".format(x, nextVal))
		x = 33 if x ==3 else x
		nextVal = x*x
		return True

	lst = [nextVal for x in [1,2,3,4] if testAndModify(x)]
	print(lst)

def main():
	test1()
	test2()

if __name__ == '__main__':
	main()