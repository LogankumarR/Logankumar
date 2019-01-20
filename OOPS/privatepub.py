class name():
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def get__pvt__var(self):
        return self.__age
    def set__pvt__var(self):
        return self.__age


def main():
    obj = name("pop",8)
    print(obj.name)
    print (obj.get__pvt__var())
    obj.set__pvt__var(10)
    print (obj.set__pvt__var())



main()
