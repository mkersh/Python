from simulator.gate import *

def make3inAndCircuit():
    if Circuit.exists("IN3_AND"):
        return Circuit.get("IN3_AND")

    c1 = Circuit("IN3_AND")
    c1.addGate("AND", 'A', 'B', 'IN1')
    c1.addGate("AND", 'IN1', 'C', 'O')
    return c1

def makeCircuit():
    if Circuit.exists("8BIT_DECODER"):
        return Circuit.get("8BIT_DECODER")

    make3inAndCircuit()
    c1 = Circuit("8BIT_DECODER")
    c1.addGate("NOT", 'A0', 'A0', 'NA0')
    c1.addGate("NOT", 'A1', 'A1', 'NA1')
    c1.addGate("NOT", 'A2', 'A2', 'NA2')

    mappings = {'A':'NA0', 'B':'NA1', 'C':'NA2', 'O':'O0'}
    c1.addCircuit("IN3_AND", mappings)
    mappings = {'A':'A0', 'B':'NA1', 'C':'NA2', 'O':'O1'}
    c1.addCircuit("IN3_AND", mappings)
    mappings = {'A':'NA0', 'B':'A1', 'C':'NA2', 'O':'O2'}
    c1.addCircuit("IN3_AND", mappings)
    mappings = {'A':'A0', 'B':'A1', 'C':'NA2', 'O':'O3'}
    c1.addCircuit("IN3_AND", mappings)
    mappings = {'A':'NA0', 'B':'NA1', 'C':'A2', 'O':'O4'}
    c1.addCircuit("IN3_AND", mappings)
    mappings = {'A':'A0', 'B':'NA1', 'C':'A2', 'O':'O5'}
    c1.addCircuit("IN3_AND", mappings)
    mappings = {'A':'NA0', 'B':'A1', 'C':'A2', 'O':'O6'}
    c1.addCircuit("IN3_AND", mappings)
    mappings = {'A':'A0', 'B':'A1', 'C':'A2', 'O':'O7'}
    c1.addCircuit("IN3_AND", mappings)


    return c1