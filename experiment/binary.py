def binaryOperators():
    binNum = 0b10
    binNum2 = 0b1
    print("{0} {0:b}".format(binNum))
    res = binNum | binNum2
    print("Bitwise OR: {op1:b} | {op2:b} = {res:b}".format(op1=binNum,op2=binNum2,res=res))
    binNum = 0b11001
    binNum2 = 0b11110
    res = binNum & binNum2
    print("Bitwise AND: {op1:b} & {op2:b} = {res:b}".format(op1=binNum,op2=binNum2,res=res))
    binNum = 0b11001
    res=~binNum # don't understand the result of this?? It doesn't look like
    print("Bitwise compliment ~ of {op:b} {res:b} check {res2:b}".format(op=binNum,res=res, res2=(-binNum - 1)))
    binNum = 0b1
    res=binNum << 1
    print("Bitwise shift << left {op:b} << 1 = {res:b}".format(op=binNum, res=res))
    binNum = 0b10
    res=binNum >> 1
    print("Bitwise shift >> right {op:b} >> 1 = {res:b}".format(op=binNum, res=res))
    binNum = 0b01011
    binNum2 = 0b10111
    res = binNum ^ binNum2 # XOR
    print("Bitwise XOR: {op1:b} ^ {op2:b} = {res:b}".format(op1=binNum,op2=binNum2,res=res))
    binNum = -3
    print("Negative number {op:b}".format(op=binNum))
    binNum = bin(~0b1111)

def complementTests():
    num1 = 10
    num2 = 5
    com = ~num2
    res = num1 & com
    print(" {op} binAdder {op2} = {res}".format(op=num1, op2=com, res=res))

def twos_comp(val, bits):
    """compute the 2's compliment of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is

def twosTests():
    binary_string = '1111' # or whatever... no '0b' prefix
    out = twos_comp(int(binary_string,2), len(binary_string))
    print(" {res}".format(res=out))
    hex_string = '0xFFFFFFFF' # or whatever... '0x' prefix doesn't matter
    out = twos_comp(int(hex_string,16), 32)
    print(" {res}".format(res=out))

def main():
    #binaryOperators()
    #complementTests()
    twosTests()
if __name__ == '__main__':
    main()