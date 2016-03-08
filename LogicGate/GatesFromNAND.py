from gate import *

def xorGateCircuit():
    """
    Shows how to make XOR from a NAND.
    MK: I doubt this is the easiest way to create an XOR from Nand gates but it works
    """
    c1 = Circuit("XOR")
    c1.addGate("NAND", 'X', 'Y', 'CIN1')
    mappings = {'X':'X', 'Y':'Y', 'Z': 'CIN2'}
    c1.addCircuit("OR", mappings)
    mappings = {'X':'CIN1', 'Y': 'CIN2', 'Z': 'Z'}
    c1.addCircuit("AND", mappings)

    return c1

def orGateCircuit():
    """
    Shows how to make OR from a NAND
    """
    c1 = Circuit("OR")
    c1.addGate("NAND", 'X', 'X', 'CIN1')
    c1.addGate("NAND", 'Y', 'Y', 'CIN2')
    c1.addGate("NAND", 'CIN1', 'CIN2', 'Z')
    return c1

def andGateCircuit():
    """
    Shows how to make AND from a NAND
    """
    c1 = Circuit("AND")
    c1.addGate("NAND", 'X', 'Y', 'CIN')
    c1.addGate("NAND", 'CIN', 'CIN', 'Z')
    return c1

def notGateCircuit():
    """
    Shows how to make NOT from a NAND
    """
    c1 = Circuit("NOT")
    c1.addGate("NAND", 'X', 'X', 'Z')
    return c1


def nandGateCircuit():
    c1 = Circuit("NAND")
    c1.addGate("NAND", 'X', 'Y', 'Z')
    return c1

def xyTruthTable(title, c):
    """
    Given a Circuit C with X, Y input lines and Z output line.
    This method will interate through all perms of x, y and display a truth table
    """
    print(title)
    print("X\tY\tZ")
    print("==========")
    for x in range(0,2):
        for y in range (0,2):
            c.setLineValue('X', x)
            c.setLineValue('Y', y)
            c.run()
            print("{0}\t{1}\t{2}".format(c.getLineValue("X"), c.getLineValue("Y"), c.getLineValue("Z")))

def xTruthTable(title, c):
    """
    Given a Circuit C with X input line and Z output line.
    This method will interate through all perms of x and display a truth table
    """
    print(title)
    print("X\tZ")
    print("======")
    for x in range(0,2):
        c.setLineValue('X', x)
        c.run()
        print("{0}\t{1}".format(c.getLineValue("X"), c.getLineValue("Z")))


def main():
    xyTruthTable("NAND Truth Table:", nandGateCircuit())
    xTruthTable("NOT Truth Table:", notGateCircuit())
    xyTruthTable("AND Truth Table:", andGateCircuit())
    xyTruthTable("OR Truth Table:", orGateCircuit())
    xyTruthTable("XOR Truth Table:", xorGateCircuit())



if __name__ == '__main__':
    main()