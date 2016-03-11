from circuits.latch import *

def dlatchIt(evTitle, c, d, e):
    c.setLineValue('D', d)
    c.setLineValue('E', e)
    c.run()
    print("{0}: D={1}\tE={2}\tQ={3}\tNQ={4}".format(evTitle, c.getLineValue("D"), c.getLineValue("E"), c.getLineValue("Q"), c.getLineValue("NQ")))

def main():
    c = srNorLatchCircuit()
    c = gatedSrLatchCircuit()
    c = dLatchCircuit()
    c = edgeTriggereddLatchCircuit()
    c.setLineValue('Q', 0)
    c.setLineValue('NQ', 1)
    dlatchIt("[ED1]", c,0,0)
    dlatchIt("[ED2]", c,1,0)
    dlatchIt("[ED3]", c,1,1)
    dlatchIt("[ED3a]", c,0,1) # Q does not change at this point. Only changes when we move from E=0 to E=1
    dlatchIt("[ED4]", c,0,0)
    dlatchIt("[ED5]", c,0,1)