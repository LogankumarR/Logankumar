# count even digits in given series
def func():
    a = eval(input("enter the length of list"))
    for i in  range(a):
               b = eval(input("enter the numbers"))
               c = []
               c.append(b)
               print (c)
    for i in  c :

        if i % 2 == 0 :
            d = []
            d.append(i)
        else :
               print ("try next")
    print ("number of even numbers is ", len(d))




func()


