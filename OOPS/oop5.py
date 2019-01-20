# methods
# intance method

class student():

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def avg(self):
        return (self.m1 + self.m2 ) / 2

    def get_m1(self):
        return (self.m1)

    def set_m1(self):
        self.m1 = 9000
        return (self.m1)


s1 = student(50,60)
s2 = student(70,90)
print (s1.avg())
print (s2.avg())
print (s1.get_m1())
print (s1.set_m1())