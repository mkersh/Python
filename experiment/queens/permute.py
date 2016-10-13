import sys
import pickle
import json
import pdb
if __name__ == '__main__':
    pathDir = "../../utils"
    sys.path.insert(0,pathDir)
from logit import *
from stopwatch import *

SW = STOPWATCH()

def getVal(total_n, perm_set, val):
    val = val % total_n
    if val not in perm_set:
        return val
    else:
        return getVal(total_n, perm_set,val+1)

def permutateAux(total_n,parent_val,num_iters,perm_list):
    if num_iters == 0:
        #DEBUG("LEAF parent={0} num_iters={1} perm={2}".format(parent_val,num_iters,perm_list))
        #assert len(perm_list) == len(set(perm_list)), "Invalid Result"
        return [perm_list]
    else:
        res = []
        perm_set = set(perm_list)
        for i in range(1,num_iters+1):
            val = getVal(total_n, perm_set, parent_val+i)
            # Having these debug statements in makes a massive difference to performance. Even when no logging DEBUG level.
            #DEBUG("RECURSE parent={0} num_iters={1} perm={2} i={3} val={4}".format(parent_val,num_iters,perm_set,i,val))
            perm_set.add(val) # I didn't have this line originally. worked for n=3 but fails for n>3
            res = res + permutateAux(total_n,val,num_iters-1,perm_list+[val])
        return res

def permutate(lst):
    n = len(lst)
    res = permutateAux(n,-1,n,[])
    # res are just permutations of range(n). We need to map back to original lst
    jsonStr = json.dumps(res)
    #DEBUG("JSON Str to replace in:\n {0}".format(jsonStr))
    for i in range(n):
        fromStr = " " + str(i)+","
        toStr = " " + str(lst[i])+"@@,"
        jsonStr = jsonStr.replace(fromStr,toStr)
        fromStr = "[" + str(i)+","
        toStr = "[" + str(lst[i])+"@@,"
        jsonStr = jsonStr.replace(fromStr,toStr)
        fromStr = " " + str(i)+"]"
        toStr = " " + str(lst[i])+"@@]"
        jsonStr = jsonStr.replace(fromStr,toStr)
        fromStr = "[" + str(i)+"]"
        toStr = "[" + str(lst[i])+"@@]"
        jsonStr = jsonStr.replace(fromStr,toStr)
        #DEBUG("After replacing {0}:\n {1}".format(i, jsonStr))
    fromStr = "@@"
    toStr = ""
    jsonStr = jsonStr.replace(fromStr,toStr)
    #DEBUG("Finished replace:\n {0}".format(jsonStr))
    perms_list = json.loads(jsonStr)
    #DEBUG("Perms:\n {0}".format(perms_list))
    return perms_list


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
    #res = permutate(range(10))
    #res = permutate(range(10))
    l1 = [1,2,3,4]
    res = permutate(l1)
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
