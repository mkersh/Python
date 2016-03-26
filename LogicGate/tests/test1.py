import sys
sys.path.insert(0,"..")

from simulator.gate import *
import circuits.adder as adder

def makeCircuit():
    c1 = Circuit("Test 1 and 0 lines")
    c1.addGate("AND", '1', '1', 'OUT1')
    return c1

def makeCircuit2():
    c = adder.makeCircuit()

    c2 = Circuit("Test 1 and 0 lines2")
    mappings = {'A':'1', 'B': '0', 'CIN': '0', 'S':'S0', 'COUT':'C0OUT'}
    c2.addCircuit("FullBitAdder", mappings)
    mappings = {'A':'0', 'B': '1', 'CIN': 'C0OUT', 'S':'S1', 'COUT':'C1OUT'}
    c2.addCircuit("FullBitAdder", mappings)
    mappings = {'A':'1', 'B': '1', 'CIN': 'C1OUT', 'S':'S2', 'COUT':'C2OUT'}
    c2.addCircuit("FullBitAdder", mappings)
    mappings = {'A':'1', 'B': '1', 'CIN': 'C2OUT', 'S':'S3', 'COUT':'C3OUT'}
    c2.addCircuit("FullBitAdder", mappings)
    return c2



def main():
	#c = makeCircuit()
    c = makeCircuit2()
    c.run()
	#c2.printAllLineValues("X0;Y0;S0;C0OUT;X1;Y1;S1;C1OUT")
    c.printAllLineValues("S0;S1;S2;S3;C3OUT")
	#TBD c2.getAllLineValues as a string. Allows you to build up a complex result to display

if __name__ == '__main__':
	main()



