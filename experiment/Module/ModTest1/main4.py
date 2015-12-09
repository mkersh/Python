# import style #1
import MyMod.file1
# import style #2
import MyMod.file1 as mod
# import style #3
from MyMod.file1 import *

"""
Import from a nested module. i.e. One contained in a sub-directory
"""

def main():
	MyMod.file1.SayHello() # Need to use full prefixing if you use import style #1
	mod.SayHello() # Can use alias for mod if you use import style #2
	SayHello() # Can refer to entities (functions, classes etc) directlry if you use inmport style #3
	
if __name__ == '__main__':
	main()