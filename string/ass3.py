#vowels in string

def string():
    a = eval(input("enter the string value"))
    vow = 0
    for m in a:
        if (m == "a" or m == "e" or m == "i" or m == "o" or m == "u"):
               vow = vow+1
        else:
               print ("try next vow")
    print (vow)

string()
