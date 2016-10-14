import sys
import json
import pdb
if __name__ == '__main__':
    pathDir = "../../utils"
    sys.path.insert(0,pathDir)
from logit import *
from stopwatch import *

SW = STOPWATCH()


# A few nasty globals to pass between permate and permutateAux. 
OrigList = []
isRange = False

def getVal(total_n, perm_set, val):
    val = val % total_n
    if val not in perm_set:
        return val
    else:
        return getVal(total_n, perm_set,val+1)


def permutateAux(total_n,parent_val,num_iters,perm_list):
    if num_iters == 0:
        # If our original list was just range(n) then we do not need to map results
        return [perm_list] if isRange else [[ OrigList[x] for x in perm_list]]
    else:
        res = []
        perm_set = set(perm_list)
        for i in range(1,num_iters+1):
            val = getVal(total_n, perm_set, parent_val+i)
            perm_set.add(val) # I didn't have this line originally. worked for n=3 but fails for n>3
            res = res + permutateAux(total_n,val,num_iters-1,perm_list+[val])
        return res

def permutate(lst):
    global OrigList, isRange # I keep having to do this?? There must be a better way
    OrigList = lst
    n = len(lst)
    rangeList = range(n)
    if str(OrigList) == str(rangeList):
        isRange = True

    res = permutateAux(n,-1,n,[])
    return res

# For debugging/testing
def checkNoDuplicates(res):
    pickled_list = set([])
    failed = False
    for x in res:
        jsonStr = json.dumps(x)
        if jsonStr in pickled_list:
            DEBUG("checkNoDuplicates: {0}".format(jsonStr))
            failed = True
        else:
            pickled_list.add(jsonStr)
    if failed:
        assert False, "Duplicate Results"

def main():
    #setLogLevel("INFO")
    setLogLevel("DEBUG")
    SW.start()
    #pdb.set_trace()
    #res = permutate(range(3))
    #res = permutate(range(4))
    #res = permutate(range(5))
    res = permutate(range(8))
    #res = permutate(range(10))
    #l1 = ['a','b','c']
    #res = permutate(l1)
    print(len(res))
    #INFO("About to print results:\n{0}".format(res))
    print(res)
    #checkNoDuplicates(res)
    #pSet = set([0,3])
    #val1 = getVal(4,pSet,4)
    #val = getVal(4,pSet,5)
    #DEBUG("getVals: {0} {1}".format(val1,val2))
    SW.stopAndPrint()

if __name__ == '__main__':
    main()
