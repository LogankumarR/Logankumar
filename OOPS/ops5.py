

class math():

    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add1_nos(self):
         return (self.a + self.b)
     def mul_nos(self):
         return (self.a * self.b)

class adv_math(math):

     z = 5
    def __init__(self,a,b):
        math.__init__(self,a,b)

    def add3_nos(self):
          print (add1_nos() + z)

    def mul3_nos(self):
          print (mul_nos * z)


obj = adv_math( 5, 5)






