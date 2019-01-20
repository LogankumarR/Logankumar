#   class method

#   if u want to create  class method for class variables u should use @classmethod oi is nothin called decoders..
#  static method
class student():

    stud = "class"

    def __init__(self,m1,m2):

        self.m1 = m1
        self.m2 = m2

    def calc(self):

        return (self.m1 + self.m2)

    @classmethod

    def info(cls):
        return (cls.stud)
   #@staticmethod
    #def inform():
       # print ("i am static method")

s1 =  student(50,40)
s2 =  student(90,100)
print (s1.calc())
print (s2.calc())
print (student.info())
