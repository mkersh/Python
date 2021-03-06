import sys
sys.path.insert(0,"..")

from simulator.gate import *
from circuits.latch import *

def latchIt(evTitle, c, r, s):
    c.setLineValue('R', r)
    c.setLineValue('S', s)
    c.run()
    print("{0}: R={1}\tS={2}\tQ={3}\tNQ={4}".format(evTitle, c.getLineValue("R"), c.getLineValue("S"), c.getLineValue("Q"), c.getLineValue("NQ")))

def glatchIt(evTitle, c, r, s, e):
    c.setLineValue('R', r)
    c.setLineValue('S', s)
    c.setLineValue('E', e)
    c.run()
    print("{0}: R={1}\tS={2}\tE={3}\tQ={4}\tNQ={5}".format(evTitle, c.getLineValue("R"), c.getLineValue("S"), c.getLineValue("E"), c.getLineValue("Q"), c.getLineValue("NQ")))

def dlatchIt(evTitle, c, d, e):
    c.setLineValue('D', d)
    c.setLineValue('E', e)
    c.run()
    print("{0}: D={1}\tE={2}\tQ={3}\tNQ={4}".format(evTitle, c.getLineValue("D"), c.getLineValue("E"), c.getLineValue("Q"), c.getLineValue("NQ")))


def main():
    c = srNorLatchCircuit()
    c.setLineValue('Q', 0)
    c.setLineValue('NQ', 1)
    latchIt("[1]", c,0,0)
    latchIt("[2]", c,0,1) # This sets Q and it is then remembered until R is set
    latchIt("[3]", c,0,0)
    latchIt("[4]", c,0,0)
    latchIt("[5]", c,1,0) # This resets the latch and this is remembered
    latchIt("[6]", c,0,0)
    latchIt("[7 - illegal]", c,1,1) # This is an illegal state. Let's see how the simulator behaves. Results in contradictions for Q and NQ
    latchIt("[8]", c,0,1)
    latchIt("[9]", c,0,0) # Seems to recover

    c.setLineValue('Q', 1)
    c.setLineValue('NQ', 1) # This is illegal as well but
    latchIt("[1a]", c,0,0)

    c = gatedSrLatchCircuit()
    c.setLineValue('Q', 0)
    c.setLineValue('NQ', 1)
    glatchIt("[G1]", c,0,0,0)
    glatchIt("[G2]", c,0,1,0)
    glatchIt("[G2]", c,0,1,1)
    glatchIt("[G2]", c,0,0,0)

    c = dLatchCircuit()
    c.setLineValue('Q', 0)
    c.setLineValue('NQ', 1)
    dlatchIt("[D1]", c,0,0)
    dlatchIt("[D2]", c,1,0)
    dlatchIt("[D3]", c,1,1)
    dlatchIt("[D3a]", c,0,1)
    dlatchIt("[D4]", c,0,0)
    dlatchIt("[D5]", c,0,1)

    c = edgeTriggereddLatchCircuit()
    c.setLineValue('Q', 0)
    c.setLineValue('NQ', 1)
    dlatchIt("[ED1]", c,0,0)
    dlatchIt("[ED2]", c,1,0)
    dlatchIt("[ED3]", c,1,1)
    dlatchIt("[ED3a]", c,0,1) # Q does not change at this point. Only changes when we move from E=0 to E=1
    dlatchIt("[ED4]", c,0,0)
    dlatchIt("[ED5]", c,0,1)

if __name__ == '__main__':
    main()