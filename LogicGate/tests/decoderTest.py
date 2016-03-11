import sys
sys.path.insert(0,"..")
import circuits.decoder as decoder

def decodeIt(c, a2,a1,a0):
    c.setLineValue('A0', a0)
    c.setLineValue('A1', a1)
    c.setLineValue('A2', a2)
    c.run()
    c.printAllLineValues("O7;O6;O5;O4;O3;O2;O1;O0")

def main():
    c = decoder.makeCircuit()
    decodeIt(c,1,1,1)



if __name__ == '__main__':
	main()



