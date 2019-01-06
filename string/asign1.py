#prime numbers


a = eval(input("Enter the number"))
b = eval(input("enter the number"))
for num  in range (a,b+1):
    if num >1 :
        if num % 2 == 0 or  num % 3 ==0:
            print ( num ,"its not  a prime number ")
        else:
            print ("\n",num,"its prime number " )
    else :
        print ("its not a prime number ")