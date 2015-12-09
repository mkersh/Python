import MyMod.SubMod.file3 as mod

"""
Import from a nested module (multiple sub-directories)
"""

def main():
	mod.SayHello() # Can use alias for mod if you use import style #2
	
if __name__ == '__main__':
	main()