"""
Hash class.

Wrote this Nov 2015 as part of my ongoing exercise to learn python.

Had fun writing it but not sure how safe it is??
That's why you would normally use a proven crypto hash function developed by mathematicians.

From basic tests I have performed though it seems to be producing relatively random results
for each input string passed.

I have also tested it over 100K iterations to prove the it doesn't generate the same hash twice.

I some point I plan to study the SHA1 (SHA256) algorithms to see the approach they take and how it differs from mine.
"""
class mj65Hash:
	_inputStream = []
	_outputStream = ['=' for x in range(256) ]
	_recordCheckPrevious = False
	_recordPreviousDict = {}
	NUMBER_LOOPS = 10
	SOME_PRIME_NUM = 797

	"""
	Allow for debug statistics to be recorded to see how the hash algorithm is performing
	"""
	def __init__(self,recordPrevious=False, recordOutputPosition=False, recordOutputChar=False):
		self._recordCheckPrevious = recordPrevious
		self._recordOutputPosition = recordOutputPosition
		self._recordOutputChar = recordOutputChar

	def execPrint(self, str):
		outStr = self.exec(str)
		trace("{0}==>{1}".format(str, outStr))
		#trace(len(outStr))
		return outStr

	def exec(self, input):
		_inputStream = []
		self._outputStream = ['=' for x in range(256) ]
		self._convertInputToList(input)
		self._padInput()
		for i in range(self.NUMBER_LOOPS):
			# Added this ability to perform the encryption a number of times
			# Without doing this, single char input would not be difficult to decrypt
			self._encrypt()
			self._inputStream = self._outputStream
		hashStr = self._convertToOutStr()
		if self._recordCheckPrevious == True:
			self.recordPreviousHash(input, hashStr)
		return hashStr

	"""
	Allow input to be a range of types.
	Convert to common list of bytes and store in 
	_inputStream
	"""
	def _convertInputToList(self, input):
		self._inputStream = list(input)

	"""
	Convert _outputStream which is a list of numbers between 0..61
	into characters
	0..25 --> A..Z
	26..51 --> a..Z
	52..62 --> 0..9
	"""
	def _convertToOutStr(self):
		# Must be a better way of doing this??
		# Either build in function to convert list to string
		# OR stringBuilder class
		# NOTE: string(lst) does work. It prints the list literally out as a string
		outStr = ""
		offVal = 0
		for x1 in self._outputStream:
			x = ord(x1)
			if x < 26:
				offVal = x
				ch = chr(ord('A') + offVal)
			elif x < 52:
				offVal = x - 26
				ch = chr(ord('a') + offVal)
			else:
				offVal = x - 52
				ch = chr(ord('0') + offVal)
			outStr += ch

		return outStr


	"""
	Pad the _inputStream to be >256
	"""
	def _padInput(self):
		if len(self._inputStream) == 0:
			# if _inputStream is empty then give it an initial value
			self._inputStream = list("@")
		while len(self._inputStream) < 256:
			self._inputStream += self._inputStream

	"""
	This is where all the magic happens
	"""
	def _encrypt(self):
		pos = 0
		for inByte in self._inputStream: 
			# This next line is really trying to mix up which of the 256 output chars
			# This particular input char will affect.
			# Not sure if the below scales though to very big input strings. Haven't tested this
			# Possibility we will blow the integer limit at somepoint
			# We could always fix this though by mod'ing the 1st expression
			outPos = ((pos * ord(inByte)) * self.SOME_PRIME_NUM) % 256
			# The above expression produces 3 times as many even positions as odd positions.
			# Let's try and even thing up by forcing it to be odd when pos is odd
			outPos = self.hackToDistributePositionMoreEvenly(pos, outPos)
			if self._recordOutputPosition == True:
				# For debug and testing purposes record the number of times each outPos is used
				# If the Hash function is to work we want full coverage of all 256 positions
				# and an even distribution (given enough calls to the hash)
				self.recordOutputPosition(outPos)
			# Originally I was doing something far simpler in terms of determining the outPos
			# This was not random enough though
			#outPos = pos % 256
			#print(outPos)
			#outChar = (outPos + ord(inByte) + ord(self._outputStream[outPos])) % 62
			#outChar = ((outPos+1) * ord(inByte) * (ord(self._outputStream[outPos])+1)) % 62
			outChar = (((outPos+1) * ord(inByte)) + (ord(self._outputStream[outPos])+1)) % 62
			if self._recordOutputChar == True:
				# For debug and testing purposes record the number of times each outPos is used
				# If the Hash function is to work we want full coverage of all 256 positions
				# and an even distribution (given enough calls to the hash)
				self.recordOutputChar(outChar)
			self._outputStream[outPos] = chr(outChar)
			pos += 1

	"""
	I am calculating which outputChar to affect using the following expression:
		outPos = ((pos * ord(inByte)) * self.SOME_PRIME_NUM) % 256

	If you use the printOutputDistribution() method though you will see that this favours 
	the even position output positions.

	To compensate for the uneven distribution of output character affected I have introduced this
	hackToDistributePositionMoreEvenly() function.

	If the pos in the input string is odd this will force the output position to be odd.
	"""
	def hackToDistributePositionMoreEvenly(self, pos, outPos):
		if (pos % 2) > 0:
			#pos is odd
			if (outPos % 2) == 0:
				# if outPos is even
				outPos += 1
		else:
			#pos is even
			if (outPos % 2) > 0:
				outPos -= 1	

		return outPos

	"""
	For debugging purposes this function looks for repeating patterns in the output
	"""
	_repeatList = set([])
	MIN_PATTERN_SIZE = 4
	def findRepeatingPatterns(self):
		self._repeatList = set([]) # Will store patterns we find in here
		outStr = self._convertToOutStr()
		pos = 1
		for ch in outStr:
			pat = ch
			rest = outStr[pos:]
			self.findRepeatAux(pat, rest)
			pos += 1
		for pat in self._repeatList:
			trace("Repeating Pattern: {0}".format(pat))

	def findRepeatAux(self, pat, str):
		
		if len(str) < 2:
			return False
		elif len(pat) < self.MIN_PATTERN_SIZE:
			newPat = pat + str[0]
			rest = str[1:]
			return self.findRepeatAux(newPat, rest) 
		# search for pat in str. If present add to list of results
		elif str.find(pat) > -1:
			# See if we can go any bigger
			newPat = pat + str[0]
			rest = str[1:]
			if self.findRepeatAux(newPat, rest) == False:
				self.checkAndAddToList(pat)
			return True
		else:
			return False

	def checkAndAddToList(self, pat):
		for it in self._repeatList:
			if len(it) >= len(pat):
				return False # bigger item already in list, just ignore
		# if we get here add pat to list
		self._repeatList.add(pat)
		return True

	_outPositionDict = {} # key = outPos, value = number of times used
	def recordOutputPosition(self, outPos):
		d = self._outPositionDict
		count = d.get(outPos,0)
		count += 1
		d[outPos] = count

	def printOutputDistribution(self):
		d = self._outPositionDict
		trace("OUTPUT POSTION USAGE")
		for pos in d:
			trace("{0} : {1}".format(pos, d[pos]))

	_outCharDict = {} # key = outPos, value = number of times used
	def recordOutputChar(self, outChar):
		d = self._outCharDict
		count = d.get(outChar,0)
		count += 1
		d[outChar] = count

	def printOutputCharUsage(self):
		d = self._outCharDict
		trace("OUTPUT CHAR USAGE")
		for pos in d:
			trace("{0} : {1}".format(pos, d[pos]))

	def recordPreviousHash(self, input, hashStr):
		# See if we have already had this hash for another input
		if self._recordPreviousDict.get(hashStr,"") != "":
			trace("CLASH of hashes. The following two inputs:")
			trace("{0}\n{1}".format(self._recordPreviousDict.get(hashStr,""),input))
			trace("BOTH produce the same hash:\n{0}".format(hashStr))
			error("stop")
		else:
			# Add to the dictionary
			self._recordPreviousDict[hashStr] = input


def error(str):
	raise Exception(str)

def trace(str):
	print(str)

def main():
	testInputs = [
		"a", "b", "c", "ab", "ba", "d", "e", "f", "g", "h", "i", "j", "k",
		"This is a more realistic example of something to hash!!",
		"Make sure we can handle strings greater than 256 in length 123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890",
		"one", "one1",
		"one two"
	]
	t1 = "a"
	t2 = "b"
	t3 = "abc"
	t4 = "Hello world Test of my Hash class!"
	# Create a big string to
	t5 = "Base for big string "
	for i in range(5000):
		t4 += str(i) + ''
	hash = mj65Hash(True, True, True) # Passing True into constructor records and checks for repeated hashes
	
	# Change the conditionals below that you want to run to True
	if False:
		hash.execPrint(t1)
		hash.findRepeatingPatterns()
	
	# The next section is useful for checking a range of test strings
	if True:
		for st in testInputs:
			hash.execPrint(st)
			hash.findRepeatingPatterns()

		# These next two lines are useful to show the distribution of positions used and Output Chars
		#hash.printOutputDistribution()
		#hash.printOutputCharUsage()

	if False:
		# I have run the below and we do not get any overlapping hashes within 100K calls
		t6 = "Some initial string to encrypt!!!"
		for i in range(10000):
			# We we then hash a number of times and look for clashes in the results produced
			if (i > 0) and (i%1000 == 0):
				print(".") # start newline
			else:
				#pass	
				print(".", end="")
			t6 = hash.exec(t6)
		print("")
		hash.printOutputDistribution()

if __name__ == '__main__':	
	main()