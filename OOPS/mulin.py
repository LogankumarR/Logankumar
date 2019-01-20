class a():

    def __init__(self):
        self.x = 0
        print ("hai i am in cons of a")

    def foo(self):
        print ("hai a")

class b():

    def __init__(self):
        self.x = 10
        print ("i am in cons of b")

    def foo(self):
        print ("hai b")

class c(b,a):

    def __init__(self):
        print ("i am in cons of c ")
        a.__init__(self)
        b.__init__(self)


    def foo(self):
        print ("hai i am in c" )


def main():
            obj = c()
            obj.foo()
            print (obj.x)
            print (obj.x)
main()
