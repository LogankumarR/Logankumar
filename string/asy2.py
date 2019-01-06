# add numbers

x = 0

def func():
    b =eval(input("enter the number"))
    for i in range(b+1):
            if i % 2 == 0:
                global x
                x = i + x
                print (x)

            else:
                print("Try next")

func()
