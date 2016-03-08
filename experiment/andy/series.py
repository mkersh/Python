
def calcSeriesSum(targetVal):
    sumSoFar = 0.0
    n = 0
    while sumSoFar <= targetVal:
        n = n + 1
        sumSoFar = sumSoFar + (1.0/n) # NOTE: On older versions of python you need 1.0 on top rather than just 1
    print ("For Sum(1/n) >  ", targetVal, "smallest k =", n)
    return n

calcSeriesSum(4)
calcSeriesSum(8)
calcSeriesSum(12)
calcSeriesSum(16)
