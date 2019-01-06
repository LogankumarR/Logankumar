class class_add():
    def __init__(self,var1,var2):
        self.atrrub1 = var1
        self.atrrub2 = var2
    def add_func(self):
         return self.atrrub1 + self.atrrub2

def main():
     obj = class_add(5,10)
     sum_var = obj.add_func()
     print ("sum of ", obj.atrrub1, "and" , obj.atrrub2, "is",sum_var )

     obj1 = class_add(100,100 )
     sum_var = obj1.add_func()
     print ("sum of ", obj1.atrrub1, "and" , obj1.atrrub2, "is",sum_var )

     obj2 =  class_add(obj.atrrub1+obj1.atrrub1,obj.atrrub2+obj1.atrrub2)#print ("sum of ", obj.atrrub1 + obj1.atrrub1, "and" , obj.atrrub2 + obj1.atrrub2 )
     sum_var = obj2.add_func()
     print("sum of ", obj2.atrrub1, "and", obj2.atrrub2, "is", sum_var)


main()




