from debug import *

def andGate(circuit, in1Line, in2Line, out1Line):
	"""(in1Line, in2Line, out1Line) refer to named lines.
	We perform a binary AND on in1Line and in2Line and store value in out1Line
	"""
	print("Basic AND gate function ")
	in1 = circuit.getLineValue(in1Line)
	in2 = circuit.getLineValue(in2Line)
	out1 = in1 and in2
	circuit.setLineValue(out1Line, out1)

class Gate:
	_circuit = None
	_gateName = ""
	_in1Line = "" 
	_in2Line = ""
	_out1Line = ""
	basicGates = ["AND", "OR", "NOT", "XOR", "NAND", "NOR"]

	def __init__(self, circuit, name, in1Line, in2Line, out1Line):
		self._circuit = circuit
		self._gateName = name
		self._in1Line = in1Line
		self._in2Line = in2Line
		self._out1Line = out1Line

		if not name in Gate.basicGates:
			error("{0} is not a valid date. \nValid gates are:\n{1}".format(name, Gate.basicGates))

	def eval(self):
		t = self._gateName
		actions = {'AND': self.evalAndGate, 'OR': self.evalOrGate, "NOT": self.evalNotGate, "XOR": self.evalXorGate, "NAND": self.evalNandGate, "NOR": self.evalNorGate  }
		actions[t]()

	def evalAndGate(self):
		c = self._circuit
		in1 = c.getLineValue(self._in1Line)
		in2 = c.getLineValue(self._in2Line)
		out1 = in1 and in2
		c.setLineValue(self._out1Line, out1)

	def evalOrGate(self):
		c = self._circuit
		in1 = c.getLineValue(self._in1Line)
		in2 = c.getLineValue(self._in2Line)
		out1 = in1 or in2
		c.setLineValue(self._out1Line, out1)

	def evalNotGate(self):
		c = self._circuit
		in1 = c.getLineValue(self._in1Line)
		out1 = int(not in1)
		c.setLineValue(self._out1Line, out1)

	def evalXorGate(self):
		c = self._circuit
		in1 = c.getLineValue(self._in1Line)
		in2 = c.getLineValue(self._in2Line)
		out1 = int(bool(in1) ^ bool(in2))
		c.setLineValue(self._out1Line, out1)

	def evalNandGate(self):
		c = self._circuit
		in1 = c.getLineValue(self._in1Line)
		in2 = c.getLineValue(self._in2Line)
		out1 = int(not (in1 and in2))
		c.setLineValue(self._out1Line, out1)

	def evalNorGate(self):
		c = self._circuit
		in1 = c.getLineValue(self._in1Line)
		in2 = c.getLineValue(self._in2Line)
		out1 = int(not (in1 or in2))
		c.setLineValue(self._out1Line, out1)

class subCircuit:
	parent = None
	circuitObj = None
	mapping = {}
	breakAfter = 0
	def __init__(self, parent, cObj, mapping):
		self.parent = parent
		self.circuitObj = cObj
		self.mapping = mapping

	def runSubCircuit(self):
		# Map parent lines to subCircuit lines
		#debug("Parent {0} subCircuit {1}".format(self.parent.name(), self.circuitObj.name()))
		#subCircuit.breakAfter += 1
		#if subCircuit.breakAfter == 2:
		#	debug("Terminating early")
		#	exit()
		self.mapSubCircuitLinesIN()
		self.circuitObj.run()
		self.mapSubCircuitLinesOUT()

	def mapSubCircuitLinesIN(self):
		for scLine in self.mapping:
			pLine = self.mapping[scLine] # determine the parent line a subCircuit line relates to
			val = self.parent.getLineValue(pLine)
			self.circuitObj.setLineValue(scLine, val)

	def mapSubCircuitLinesOUT(self):
		for scLine in self.mapping:
			pLine = self.mapping[scLine] # determine the parent line a subCircuit line relates to
			val = self.circuitObj.getLineValue(scLine)
			self.parent.setLineValue(pLine,val)




class Circuit(object):
	"""Digital circuit simulator"""

	_basic_gates = {"AND": andGate}
	_all_circuits = {} #  map of all circuits
	_gates = [] # Stores the gates or Circuit in this Circuit 
	_subCircuit = []
	_lines = {} # Stores the lines that act as input and/or output for the gates and circuits

	def all():
		""" return all circuits dictionary"""
		return Circuit._all_circuits

	def __init__(self, name):
		self._gates = []
		self._subCircuit = []
		self._lines = {}
		if not Circuit._all_circuits.get(name) is None:
			error("Circuits must have a unique name!!")
		else:
			Circuit._all_circuits[name] = self
			self._name = name

	def name(self):
		return self._name

	def getLineValue(self, lineName):
		return self._lines.get(lineName,0)

	def setLineValue(self, lineName, lineValue):
		self._lines[lineName] = lineValue

	def addGate(self, gate, in1Line, in2Line, out1Line):
		"""Add a logic gate to this Circuit"""
		self._gates.append( Gate(self, gate, in1Line, in2Line, out1Line))
		


	def addCircuit(self, cname, mappings):
		"""Add a subCircuit to this Circuit. 
		cname - Name of subCircuit to add. Must exist in Circuit.all()
		mappings - is a map of line mappings from subCircuit to parentCircuit
			mappings key is the subCircuit line name. value is the corresponding parent line
		"""
		cobj = Circuit.all()[cname]
		#debug("addCircuit: {0}-->{1}".format(self.name(),cobj.name()))
		self._subCircuit.append(subCircuit(self,cobj,mappings.copy()))

	def run(self):
		cycleIter = 1
		"""Run the Cicuit"""
		#debug("running {0}".format(self.name()))
		while True:
			previousLines = self._lines.copy()
			self.cycle(cycleIter)
			if self.haveLinesChanged(previousLines) == False:
				#debug("Finish Run")
				#print ("previous: {0}".format(previousLines))
				#print ("now: {0}".format(self._lines))
				break
			elif cycleIter > 100:
				assert False, "Circuit.run - Too many iterations"
			cycleIter += 1
		#debug("END running {0}".format(self.name()))


	def haveLinesChanged(self, previousLines):
		newLines = self._lines
		for k in newLines:
			if newLines[k] != previousLines.get(k):
				return True
		return False

	def cycle(self, cycleIter):
		#trace("cycle {0}".format(cycleIter))
		for g in self._gates:
			g.eval()
		for sc in self._subCircuit:
			sc.runSubCircuit()
		return True

	def printAllLineValues(self, toPrint=""):
		if toPrint != "":
			#keys = self._lines.keys()
			keys = toPrint.split(";")
		else:
			keys = self._lines.keys()
		for key in keys:
			print("{0} = {1}".format(key,self._lines[key]))

def main():
	assert True, "This should not fail"
	c1 = Circuit("c1")
	#c2 = Circuit("c2")
	#c3 = Circuit("c3")
	#c4 = Circuit("c4")
	#for circuitName, circuitObj in Circuit.all().items():
		#print("{0} - {1}".format(circuitName, circuitObj.name()))
	
	c1.setLineValue('I1', 0)
	c1.setLineValue('I2', 1)
	c1.addGate("AND", 'I1', 'I2', 'O1')
	c1.addGate("OR", 'I1', 'I2', 'O2')
	c1.addGate("NOT", 'O1', 'I1', 'O3')
	c1.addGate("NOR", 'O1', 'O2', 'O4')
	c1.addGate("XOR", 'I1', 'I2', 'O5')
	c1.run()
	print("O1 = {0}".format(c1.getLineValue("O1")))
	print("O2 = {0}".format(c1.getLineValue("O2")))
	print("O3 = {0}".format(c1.getLineValue("O3")))
	print("O4 = {0}".format(c1.getLineValue("O4")))
	print("O5 = {0}".format(c1.getLineValue("O5")))




if __name__ == '__main__':
	main()




		
		