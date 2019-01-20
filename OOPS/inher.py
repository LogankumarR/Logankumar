class vechicle():
    def __init__(self,log):
        self.color = green_
class car(vechicle):
    def __init__(self,brand):
        self.brd = brand
        vechicle.__init__(self,"red")
def main():
    obj = car("honda")
    print (obj.brd)
    print(obj.color)

main()

