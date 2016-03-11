import sys

breakAfter = 0

# Below are for printing colour to a terminal. Doesn't work in the Sublime terminal though
# e.g bcolors.FAIL + "some text" + bcolors.ENDC
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def testfunc():
	print("Yes it works!!")

def error(str):
	raise AssertionError(str) 
	#sys.exit() # Raise an exception instead. This way we can test

def trace(str):
    print(str)

def debug(str):
	print(str)

def exit():
    sys.exit()
