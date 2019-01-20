# types of variable in oops

 #one is class variable and another one is instance variable

 # variable is defined inside class that is instance variable beacuse it will vary according to object

 # class variables which we should declare outside of class but it is shared to all other objets

# let see one example

class car():

    #class variable

    wheels = 10

    def __init__(self,type,year):
        self.types = type             #...> instance variable
        self.years = year
    def func(self):
        print (self.types,self.years)


car1 = car("honda",1995)
car2 = car("skoda",1996)
car1.func()
car2.func()
print (car1.wheels)
print (car2.wheels)


