def main():

    class c1:
        def __init__(self):
            pass
    class c2(c1):
        def __init__(self):
            pass
    a = 1
    b = []
    c = {}
    d = {'k1':12}
    e = {1,2,3,4}
    f = (1,)
    g = (2)
    h = c1()
    i = c2()
    print("1", type(1))
    print("a=1", type(a))
    print("b", type(b))
    print("c", type(c))
    print("d", type(d))
    print("e", type(e))
    print("f", type(f))
    print("g", type(g))
    print("c1", type(c1))
    print("c2", type(c2))
    print("h", type(h))
    print("i", type(i))

    if isinstance(i, c1):
        print("yes i isinstance of c1")


if __name__ == '__main__':
    main()