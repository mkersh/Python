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
	debugger = rpdb.Rpdb(port=12345) # rather than use standard port specify your own
	debugger.set_trace()
	testFunc()

if __name__ == '__main__':
	main()

