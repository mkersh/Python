import sys

"""
Print out sys.path. 

This shows all the places that python will look for modules.

These places consist of:
1) built in modules
2) Directory of the input script (current directory)
3) PYTHONPATH - PATH style list of directories
4) Installation dependent defaults

Some interesting things from #4 (on my windows machine):
- *.egg files
- *.zip files
- DLLs

Look at /cygdrive/c/Python34/lib/site.py to find out more about how python sets the sys.path
These are experiments for another day.
 
"""
def main():
	print("Path for python picking up modules from")
	print(sys.path)
	
if __name__ == '__main__':
	main()