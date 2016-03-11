# I don't need to do it this way, just experimenting with dynamic loading of modules
def loadAndRun(name):
    mod = __import__(name, fromlist=[''])
    mod.main()

def main():
    #loadAndRun("tests.adderTest")
    #loadAndRun("tests.GatesFromNAND")
    #loadAndRun("tests.forever")
    #loadAndRun("tests.latchTest1")
    #loadAndRun("tests.latch1")
    loadAndRun("tests.decoderTest")

if __name__ == '__main__':
    main()