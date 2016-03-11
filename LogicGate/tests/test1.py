import sys
def addPath(path):
    if str(sys.path).find(path) == -1:
        sys.path.insert(0,path)
addPath("../simulator")
addPath("../circuits")
from latch import *

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


if __name__ == '__main__':
    main()