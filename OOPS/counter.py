class abc():
    count = 0
    def __init__(self,var1 =1,var2 ="pop")
          self.arg1 = var1
          self.arg2 = var2
          abc.count = abc.count + 1
          print ("in constructor")
    def print_obj(self):
        print("object" , self.arg1)
        print ("object", self.arg2)
    def __del__(self):
        print ("destructor called")
        abc.count = abc.count - 1
def main()
    obj1 =abc(l1,"pop")
    print(abc.count)
    obj2 = abc(12,"lol")
    print(abc.count)

main()

        
