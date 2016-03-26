import sys
sys.path.insert(0,"..")

from simulator.gate import *
import circuits.bcdAdder as bcdAdder

def main():
    c = bcdAdder.makeCircuit()
    c.setLineValue('CIN', 0)
    c.setLineValue('X0', 1),c.setLineValue('X1', 0),c.setLineValue('X2', 0),c.setLineValue('X3', 1)
    c.setLineValue('Y0', 1),c.setLineValue('Y1', 0),c.setLineValue('Y2', 0),c.setLineValue('Y3', 1)
    c.run()
    c.printAllLineValues("S0;S1;S2;S3;COUT")

if __name__ == '__main__':
    main()



