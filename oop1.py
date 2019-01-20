class emp():

    def __init__(self,name,age,salary):
        self.names = name
        self.ages = age
        self.salarys = salary

    def func1(self):
        print ("details", self.names, self.ages, self.salarys )


obj  = emp("logan",25,25000)
obj2 = emp("loga",35,35000)
obj.func1()
obj2.func1()