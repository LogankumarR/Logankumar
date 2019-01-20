# class inside class nothing but  inner  class

class outc():

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        self.l1 = self.inc

    def show(self):

        print (self.m1 + self.m2)
][[][]]       self.l1.show2()

    class inc():

            def __init__(self):
                self.brand = "hp"

            def show2(self):
                print (self.brand)

obj1 = outc(20,30)
obj2 = outc(20,50)

obj1.show()