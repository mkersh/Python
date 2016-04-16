
class MyClass:
    """A simple class"""
    i = 123 # class level member
    def __init__(self):
        """Constructor"""
        pass
    def f(self):
        return 'hello world'
    @classmethod
    def clsMeth(cls): # You can call with either cls.clsMeth or obj.clsMeth
        return cls.i
    @staticmethod
    def staticMeth(): # Does not take any ref to obj or cls
        return 'static method'

class Class2(MyClass):
    def __init__(self):
        """Constructor"""
        super(Class2, self).__init__()
        #Base.__init__(self, value = 20)
        #Doesn't behalf well for multiple inheritence
        pass

def printAll(idesc):
    print(idesc)
    print("obj1.i", obj1.i)
    print("obj2.i", obj2.i)

def main():
    global obj1, obj2
    obj1 = MyClass()
    obj2 = MyClass()
    obj1.i = 777     # This is changed just for obj1
    printAll("step 1")
    del obj1.i
    printAll("step 2 - after del")
    MyClass.i = 777 # Change the class default
    printAll("step 3 - changed class default")
    obj1.i = 234
    print("Call class method", obj1.clsMeth())
    print("Call class method", MyClass.clsMeth())
    print("Call static method", obj1.staticMeth())
    print("Call static method", MyClass.staticMeth())
    obj3 = Class2()
    print("Call class method obj3", obj3.clsMeth())
if __name__ == '__main__':
    main()