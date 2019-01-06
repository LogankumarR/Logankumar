# vowels excluding

#overwitten....?


def func():
           a = eval(input("enter the string"))
           for j in a :
                if (j == "a" or j == "e" or j == "i" or j == "o" or j == "u"):
                    a = a.replace(j ," ")
                else:
                    print ("try next")
           print (a)

func()
