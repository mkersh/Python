import sys
sys.path.insert(0,"..")

from simulator.gate import *
import circuits.adder as adder

def main():
	c = adder.makeCircuit()

	c.setLineValue('0', 0)
	c.setLineValue('X0', 0),c.setLineValue('X1', 1),c.setLineValue('X2', 1),c.setLineValue('X3', 0)
	c.setLineValue('Y0', 0),c.setLineValue('Y1', 1),c.setLineValue('Y2', 0),c.setLineValue('Y3', 0)

	c.run()
	#c2.printAllLineValues("X0;Y0;S0;C0OUT;X1;Y1;S1;C1OUT")
	c.printAllLineValues("S0;S1;S2;S3")
	#TBD c2.getAllLineValues as a string. Allows you to build up a complex result to display

if __name__ == '__main__':
	main()



