from simulator.gate import *
import circuits.adder as adder


def makeCircuitAux():
    """
    See makeCircuit() below for the fill BCDAdder circuit.
    makeCircuit() handles carry in (CIN)

    INPUTS
    ======
    X0, X1, X2, X3  - 1st BCD number
    Y0, Y1, Y2, Y3  - 2nd BCD number

    OUTPUTS
    =======
    S0, S1, S2, S3  - BCD Result
    COUT            - Carry Out

    """
    c = adder.makeCircuit()

    c1 = Circuit("BCDAdderNoCarryIn")

    mappings = {
        'X0':'X0','X1':'X1','X2':'X2','X3':'X3',
        'Y0':'Y0','Y1':'Y1','Y2':'Y2','Y3':'Y3',
        'S0':'S0_1','S1':'S1_1','S2':'S2_1','S3':'S3_1',
        'COUT':'COUT1'}
    c1.addCircuit("4BitAdder", mappings)

    # If S(0-3) > 9 then add 6 to it
    c1.addGate("OR", 'S0_1', 'S1_1', 'OR1')
    c1.addGate("OR", 'S2_1', 'OR1', 'OR2')
    c1.addGate("AND", 'S3_1', 'OR2', 'ADD6_1')  # if S(0-3) > 9 or COUT1 = 1 then we need to add 6
    c1.addGate("OR", 'ADD6_1', 'COUT1', 'ADD6') # ADD6 = 1 means we need to add 6 to the result
    c1.addGate("AND", '0', 'ADD6', 'SIX0') # SIX(0-3) will represent BCD 6 when ADD6 is high else 0
    c1.addGate("AND", '1', 'ADD6', 'SIX1')
    c1.addGate("AND", '1', 'ADD6', 'SIX2')
    c1.addGate("AND", '0', 'ADD6', 'SIX3')

    mappings = {
        'X0':'S0_1','X1':'S1_1','X2':'S2_1','X3':'S3_1',
        'Y0':'SIX0','Y1':'SIX1','Y2':'SIX2','Y3':'SIX3',
        'S0':'S0','S1':'S1','S2':'S2','S3':'S3',
        'COUT':'COUT2'}
    c1.addCircuit("4BitAdder", mappings)
    c1.addGate("OR", 'COUT1', 'COUT2', 'COUT')

    return c1

def makeCircuit():
    """
    INPUTS
    ======
    CIN             - Carry IN
    X0, X1, X2, X3  - 1st BCD number
    Y0, Y1, Y2, Y3  - 2nd BCD number

    OUTPUTS
    =======
    S0, S1, S2, S3  - BCD Result
    COUT            - Carry Out

    """
    c = makeCircuitAux()

    c1 = Circuit("BCDAdder")

    mappings = {
        'X0':'X0','X1':'X1','X2':'X2','X3':'X3',
        'Y0':'Y0','Y1':'Y1','Y2':'Y2','Y3':'Y3',
        'S0':'S0_1','S1':'S1_1','S2':'S2_1','S3':'S3_1',
        'COUT':'COUT1'}
    c1.addCircuit("BCDAdderNoCarryIn", mappings)

    # If CIN = 1 then add 1 to the result
    c1.addGate("AND", '1', 'CIN', 'ONE0') # ONE(0-3) will represent BCD 1 when CIN is high else 0
    c1.addGate("AND", '0', 'CIN', 'ONE1')
    c1.addGate("AND", '0', 'CIN', 'ONE2')
    c1.addGate("AND", '0', 'CIN', 'ONE3')

    mappings = {
        'X0':'S0_1','X1':'S1_1','X2':'S2_1','X3':'S3_1',
        'Y0':'ONE0','Y1':'ONE1','Y2':'ONE2','Y3':'ONE3',
        'S0':'S0','S1':'S1','S2':'S2','S3':'S3',
        'COUT':'COUT2'}
    c1.addCircuit("BCDAdderNoCarryIn", mappings)

    c1.addGate("OR", 'COUT1', 'COUT2', 'COUT')

    return c1

