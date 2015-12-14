"""
Testing out https://pypi.python.org/pypi/rpdb/
"""
import rpdb

def testFunc():
	print("line 1")
	print("line 2")
	print("line 3")
	print("line 4")

def main():
	print("Before stop in debugger")
	rpdb.set_trace() # The debugger port by default is 4444
	testFunc()

if __name__ == '__main__':
	main()

