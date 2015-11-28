"""
Hash class
"""
class mj65Hash:
	_inputStream = []
	_outputStream = ['A' for x in range(256) ]
	NUMBER_LOOPS = 1

	def execPrint(self, str):
		outStr = self.exec(str)
		trace("{0}==>{1}".format(str, outStr))
		trace(len(outStr))

	def exec(self, input):
		self._convertInputToList(input)
		self._padInput()
		for i in range(self.NUMBER_LOOPS):
			self._encrypt()
			self._inputStream = self._outputStream
		return self._convertToOutStr()

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
				ch = chr(ord('a') + offVal)
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
			outPos = pos % 256
			outChar = (outPos + ord(inByte) + ord(self._outputStream[outPos])) % 62
			self._outputStream[outPos] = chr(outChar)
			pos += 1

	"""
	For debugging purposes this function looks for repeating patterns in the output
	"""
	_repeatList = set([])
	MIN_PATTERN_SIZE = 4
	def findRepeatingPatterns(self):
		_repeatList = [] # Will store patterns we find in here
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


def error(str):
	raise Exception(str)

def trace(str):
	print(str)

def main():
	t1 = "a"
	t2 = "b"
	t3 = "Hello world Test of my Hash class!"
	# Create a big string to
	t4 = "Base for big string "
	for i in range(5000):
		t4 += str(i) + ''
	hash = mj65Hash()
	hash.execPrint(t1)
	hash.findRepeatingPatterns()
	#hash.execPrint(t2)
	#hash.execPrint(t3)
	

if __name__ == '__main__':	
	main()