from gate import *

def main():
	c1 = Circuit("FullBitAdder")
	c1.setLineValue('A', 1)
	c1.setLineValue('B', 1)
	c1.setLineValue('CIN', 1)
	c1.addGate("XOR", 'A', 'B', 'INT1')
	c1.addGate("XOR", 'INT1', 'CIN', 'S')
	c1.addGate("AND", 'INT1', 'CIN', 'INT2')
	c1.addGate("AND", 'A', 'B', 'INT3')
	c1.addGate("OR", 'INT2', 'INT3', 'COUT')

	c2 = Circuit("4BitAdder")
	c2.setLineValue('0', 0)
	c2.setLineValue('X0', 0),c2.setLineValue('X1', 1),c2.setLineValue('X2', 1),c2.setLineValue('X3', 0)
	c2.setLineValue('Y0', 0),c2.setLineValue('Y1', 1),c2.setLineValue('Y2', 0),c2.setLineValue('Y3', 0)
	mappings = {'A':'X0', 'B': 'Y0', 'CIN': '0', 'S':'S0', 'COUT':'C0OUT'}
	c2.addCircuit("FullBitAdder", mappings)
	mappings = {'A':'X1', 'B': 'Y1', 'CIN': 'C0OUT', 'S':'S1', 'COUT':'C1OUT'}
	c2.addCircuit("FullBitAdder", mappings)
	mappings = {'A':'X2', 'B': 'Y2', 'CIN': 'C1OUT', 'S':'S2', 'COUT':'C2OUT'}
	c2.addCircuit("FullBitAdder", mappings)
	mappings = {'A':'X3', 'B': 'Y3', 'CIN': 'C2OUT', 'S':'S3', 'COUT':'C3OUT'}
	c2.addCircuit("FullBitAdder", mappings)

	c2.run()
	#c2.printAllLineValues("X0;Y0;S0;C0OUT;X1;Y1;S1;C1OUT")
	c2.printAllLineValues("S0;S1;S2;S3")
	#TBD c2.getAllLineValues as a string. Allows you to build up a complex result to display

if __name__ == '__main__':
	main()