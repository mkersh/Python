import mod1 as m

"""
Giving the module an alias.
You then have to use this alias when referencing.
Referencing via mod1 below will not work.
"""

def main():
	m.SayHello()
	
if __name__ == '__main__':
	main()