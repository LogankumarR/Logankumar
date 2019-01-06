#list
l=["hai",1,2,3]
print (l)
#acces
print (l[1])
#change
l[1] = "lk"
print (l)
#for
for x in l:
    print (x)
print (len(l))
a=[1,2,3,4]
#mem check
print (5 not in a)
#append
print (a.append(99))
print (a)
#insert at specified loaction
print (a.insert(4,"logi"))
print (a)
#remove
print (a.remove(99))
print (a)
#pop
print (a.pop())
print (a)
#pop with index
print (a.pop(2))
print (a)
#del
i= [1,2,"robo"]
del i[1]
print (i)
#del
 # del i
  # print (i) it will show error
#clear
j = [1,2,3]
j.clear()
print (j)
#listconstructor
a = list(("hai","logan"))
print (a)
#copy
l =[1,2,3]
z = l
print (z)
z.append(4)
print (z)
print (l)
#shallow copy
p =[1,2,3]
s = p.copy()
s.append(5)
print (s)
print (p)
#slice opertaor
o = [6,7]
c = o[:]
c.append(10)
print (c)
print (o)
#extend
a = [1,2,3]
b = [4,5]
a.extend(b)
print (a)
#add diff data types
z = [4,5,6]
d = (1,2,3)
z.extend(d)
print (z)
# +=
a =[1,2,3]
b = [4,5,6]
a += b
print (a)
#reversed
a= [1,2,3,4]
a.reverse()
print (a)
#slice operator
a =[1,2,3,4,5]
b = a[::-1]
print (b)
#reversed
x=[5,6,7]
for i in reversed(x):
 print (i)
#sort
a =[1,2,9,3,10,5]
a.sort()
print (a)
#decs
l=[1,2,3,4,5]
l.sort(reverse = True)
print (l)
