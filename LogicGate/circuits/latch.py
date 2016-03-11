from simulator.gate import *

def edgeTriggereddLatchCircuit():
    """
    edgeTrigger D Latch Circuit
    """
    if Circuit.exists("EDGE_D_LATCH"):
        return Circuit.get("EDGE_D_LATCH")

    c1 = Circuit("EDGE_D_LATCH")
    c1.addGate("NOT", 'E', 'E', 'NE')

    mappings = {'D':'D', 'E':'NE', 'Q':'Q1', 'NQ':'NQ1'}
    c1.addCircuit("D_LATCH", mappings)

    mappings = {'D':'Q1', 'E':'E', 'Q':'Q', 'NQ':'NQ'}
    c1.addCircuit("D_LATCH", mappings)

    return c1

def dLatchCircuit():
    """
    Gated D Latch Circuit
    """
    if Circuit.exists("D_LATCH"):
        return Circuit.get("D_LATCH")

    c1 = Circuit("D_LATCH")
    c1.addGate("NOT", 'D', 'D', 'ND')

    mappings = {'R':'ND', 'S':'D', 'E':'E', 'Q':'Q', 'NQ':'NQ'}
    c1.addCircuit("GATED_SR_LATCH", mappings)

    return c1

def gatedSrLatchCircuit():
    """
    Gated SR Latch Circuit
    """
    if Circuit.exists("GATED_SR_LATCH"):
        return Circuit.get("GATED_SR_LATCH")

    c1 = Circuit("GATED_SR_LATCH")
    c1.addGate("AND", 'R', 'E', 'IN1')
    c1.addGate("AND", 'S', 'E', 'IN2')

    mappings = {'R':'IN1', 'S':'IN2', 'Q':'Q', 'NQ':'NQ'}
    c1.addCircuit("SR_NOR_LATCH", mappings)

    return c1

def srNorLatchCircuit():
    """
    SR NOR Latch Circuit
    """
    if Circuit.exists("SR_NOR_LATCH"):
        return Circuit.get("SR_NOR_LATCH")

    c1 = Circuit("SR_NOR_LATCH")
    c1.addGate("NOR", 'R', 'NQ', 'Q')
    c1.addGate("NOR", 'S', 'Q', 'NQ')
    return c1
