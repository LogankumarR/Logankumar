# how to compare to different objects

class emp():

    def __init__(self,name,age,salary):
        self.names = name
        self.ages = age
        self.salarys = salary

    def func1(self):
        print ("details", self.names, self.ages, self.salarys )

    def compare(self,other):
        if self.ages == other.ages :
            print ("same")
        else:
            print("no")

obj  = emp("logan",25,25000)
obj2 = emp("loga",25,35000)
obj.func1()
obj2.func1()
obj.compare(obj2)