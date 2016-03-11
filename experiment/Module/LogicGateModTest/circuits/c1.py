# Next two lines needed if you want to execute this file directly
#import sys
#sys.path.insert(0,"..")

from simulator.sim import *
import circuits.c2 as c2

def makeCircuit():
    print("c1 make Circuit")
    simulator("from c1")
    c2.makeCircuit()
def main():
    print("c1 main called")
    makeCircuit()
if __name__ == '__main__':
    main()