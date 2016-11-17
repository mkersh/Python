# Just want to do a simple experiment with a simple mutable Tree data structure in Python
# This is to compare it with an immutable version that I have created in haskell https://github.com/mkersh/HaskellTests/blob/master/tree.hs 

# To keep things simple I will just use a dictionary to represent Trees
# The dictionary will have the following keys: {val:"Node value", left, right: <other obj or None)}

def singleton(val):
    return {"val": val, "left": None, "right": None}

# Our data structure is an unbalanced binary Tree
# worst case insertion O(n), best case (if balanced) O(log n)
# We only ever create a single new node though. This is not the same if we have a immutable version of the data structure.
def insertMut(val, tree):
    if tree == None:
        assert False, "You need to pass a Tree to this routine"
    elif val <= tree["val"]:
        if tree["left"] == None:
            tree["left"] = singleton(val)
        else:
            insertMut(val, tree["left"])
    else:
        if tree["right"] == None:
            tree["right"] = singleton(val)
        else:
            insertMut(val, tree["right"])

def createTree(val, left=None, right=None):
    return {"val": val, "left": left, "right": right}

# Here's an immutable version for comparision
# In pure Functional languages (like Haskell) immutable data structures are the norm. You have to go out of your way to
# to create an immutable structure
def insertImut(val,tree):
    if tree == None:
        return singleton(val)
    elif val <= tree["val"]:
        # In the immutable version we have to build a new tree. This is done by calling createTree(...)
        # NOTE: The recursive call to insertImut to either the left or the right branch.
        # If a branch does not change we can reuse the existing branch
        # If the tree is balanced (not guarenteed with this DS) then (log n) new tree nodes need to be created to create the new tree
        # With these unbalanced trees worst case n new tree nodes are needed to copy
        return createTree(tree["val"],insertImut(val,tree["left"]), tree["right"])
    else:
        return createTree(tree["val"], tree["left"], insertImut(val,tree["right"]))

def testMutaableVersion():
    print("Testing Mutable binary Tree insert")
    x = singleton(1)
    insertMut(2,x)
    insertMut(20,x)
    insertMut(5,x)
    insertMut(5,x)
    print(x)

def testImmutaableVersion():
    print("Testing Immutable binary Tree insert")
    x = singleton(1)
    x = insertImut(2,x)
    x = insertImut(20,x)
    x = insertImut(5,x)
    x = insertImut(5,x)
    print(x)

def main():
    testMutaableVersion()
    testImmutaableVersion()

if __name__ == '__main__':
    main()