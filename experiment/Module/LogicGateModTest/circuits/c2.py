# Next two lines needed if you want to execute this file directly
#import sys
#sys.path.insert(0,"..")

from simulator.sim import *

def makeCircuit():
    print("c2 make Circuit")
    simulator("c2")
def main():
    print("c2 main called")
    makeCircuit()
if __name__ == '__main__':
    main()