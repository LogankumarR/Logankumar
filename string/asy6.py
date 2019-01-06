# list to tuple

def func():
    a = []
    b = eval(input("enter the length of list"))
    for i in range(b):
        c = eval(input("enter the element"))
        a.append(c)
    print (a)
    print ("after changed to tuple")
    z = tuple(a)
    print (z)

func()

