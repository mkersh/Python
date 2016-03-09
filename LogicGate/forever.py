from gate import *

def foreverCircuit():
    """
    Circuit that never stabilises its outputs.

    This didn't fail in the way I thought. It only does if X=0 which reduces it to a Feedback Not.
    To debug this enable trace on the Circuit.run() method. Need to change gate.py to do this
    """
    c1 = Circuit("NOT_FEEDBACK")
    c1.addGate("OR", 'X', 'Z', 'IN1')    # This turns out to be redundant. It onlt runs forever when X=0
    c1.addGate("NOT", 'IN1', 'IN1', 'Z')
    return c1

def foreverCircuit2():
    """
    Another Circuit that never stabilises its outputs. Again only in one situation
    """
    c1 = Circuit("NOT_FEEDBACK2")
    c1.addGate("AND", 'X', 'Z', 'IN1')    # This turns out to be redundant. It onlt runs forever when X=0
    c1.addGate("NOT", 'IN1', 'IN1', 'Z')
    return c1

def foreverCircuit3():
    """
    Another Circuit that never stabilises its outputs. Again only in one situation
    """
    c1 = Circuit("NOT_FEEDBACK3")
    c1.addGate("XOR", 'X', 'Z', 'IN1')
    c1.addGate("NOT", 'IN1', 'IN1', 'Z')
    return c1

def runCircuit(title, c):
    try:
        c.run()  # Not expecting this to stabilise and return
    except:
        print("{0}:DID NOT TERMINATE".format(title))
    else:
        print("{0}:FINISHED".format(title))

def main():
    c = foreverCircuit()
    c.setLineValue('Z', 0)
    c.setLineValue('X', 0)
    runCircuit("foreverCircuit X=0", c)
    c.setLineValue('Z', 0)
    c.setLineValue('X', 1)
    runCircuit("foreverCircuit X=1", c)
    c = foreverCircuit2()
    c.setLineValue('Z', 0)
    c.setLineValue('X', 0)
    runCircuit("foreverCircuit2 X=0", c)
    c.setLineValue('Z', 0)
    c.setLineValue('X', 1)
    runCircuit("foreverCircuit2 X=1", c)

    c = foreverCircuit3()
    c.setLineValue('Z', 0)
    c.setLineValue('X', 0)
    runCircuit("foreverCircuit3 X=0", c)
    c.setLineValue('Z', 0)
    c.setLineValue('X', 1)
    runCircuit("foreverCircuit3 X=1", c)


if __name__ == '__main__':
    main()