import MyMod.SubMod.file3 as mod
import MyMod.SubMod.file3			# importing in 3 different ways to test that __init__ gets called once
from MyMod.SubMod.file3 import *
import MyMod.SubMod as s

"""
What's the purpose of the module __init__.py file.

These get executed whenever a module is loaded.
Let's add one for SubMod.

NOTE: The __init__.py only get's executed once
"""

def main():
	mod.SayHello() # Can use alias for mod if you use import style #2
	s.SayHello()
	
if __name__ == '__main__':
	main()