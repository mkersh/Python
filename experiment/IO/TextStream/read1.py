"""
Ref: https://docs.python.org/3/library/io.html#io.TextIOBase
"""
import io

TEST_FILE1 = "files/file1.txt"
TEST_FILE2 = "files/file1-utf16.txt"
TEMP_TEST_FILE1 = "files/tmpfile2.txt" # Gets written and modified by tests below

def readfileInOne(fpath, encoding="utf-8", size=None):
	fs = open(fpath,"r", encoding=encoding)  # NOTE: Have to pass encoding as a named parameter cos it is not 3rd positional one
	fileStr = fs.read(size) # positive 1st param indicates how many chars to read
	print("Contents of {0}:".format(TEST_FILE1))
	print(fileStr)

def readfileLineByLine1(fpath, encoding="utf-8"):
	fs = open(fpath,"r", encoding=encoding) 
	print("readfileLineByLine1: Contents of {0}".format(fpath))
	for l in lineGenerator(fs):
		print(l)

def lineGenerator(fstream):
	i = 1
	line = fstream.readline()
	while line:
		print("yield line {0}".format(i))
		yield line
		line = fstream.readline()
		i += 1
	return

def readfileLineByLine2(fpath, encoding="utf-8"):
	fs = open(fpath,"r", encoding=encoding) 
	print("readfileLineByLine2: Contents of {0}".format(fpath))
	i = 1
	for l in fs:
		print("{0} {1}".format(i,l))
		i += 1

def readFromStrBuffer():
	f = io.StringIO("Line1\nLine2\nLine3\nLine4")
	print("readFromStrBuffer: ")
	i = 1
	for l in f:
		print("{0} {1}".format(i,l))
		i += 1

def modStrBuffer():
	"""The official documentation says that the offset you pass to seek must have come from a tell() call.
	Seems to work below though on a IO Text stream
	"""
	f = io.StringIO("Line1\nLine2\nLine3\nLine4")
	print("modStrBuffer: ")
	f.seek(3, 0)
	print("777",file=f) # This will trample over existing content in the file at this position
	f.seek(0, 0)
	i = 1
	for l in f:
		print("{0} {1}".format(i,l))
		i += 1

def modFile(fpath, fpath2, encoding="utf-8"):
	"""Wonder if windows is different from unix here.
    The forumns are saying you can't modify a text file directly but it seems to work below (on windows)
	"""
	fs = open(fpath,"r", encoding=encoding)  # NOTE: Have to pass encoding as a named parameter cos it is not 3rd positional one
	fileStr = fs.read(None) # positive 1st param indicates how many chars to read
	
	wfs = open(fpath2,"w", encoding=encoding) # w overwrites any existing content
	#wfs = open(fpath2,"r+", encoding=encoding) # r+ allows us to read and write to the file
	#wfs = open(fpath2,"a", encoding=encoding) # a appends to the end
	#wfs = open(fpath2,"a+", encoding=encoding) # a+ appends to the end but allows independent seeking backwards to read
	wfs.write(fileStr)
	wfs.close()

	# Now let's open again and try and modify
	wfs = open(fpath2,"r+", encoding=encoding)
	wfs.seek(3,0)
	print("888",file=wfs)
	wfs.seek(0, 0)

	print("modFile: Contents of {0}".format(fpath2))
	i = 1
	for l in wfs:
		print("{0} {1}".format(i,l))
		i += 1
	

def main():
	#readfileInOne(TEST_FILE1)
	#readfileInOne(TEST_FILE2, encoding="utf-16") # file needs to be encoded with a BOM. BOM = Header that tells us the endianess of the file
	#readfileInOne(TEST_FILE1, size=3) # reads 2 characters from the file

	#readfileLineByLine1(TEST_FILE1) # This is the hard way to do it but it shows an example of a generator function (using yeild)
	#readfileLineByLine2(TEST_FILE1)
	#readFromStrBuffer()
	#modStrBuffer()
	modFile(TEST_FILE1, TEMP_TEST_FILE1)

if __name__ == '__main__':
	main()