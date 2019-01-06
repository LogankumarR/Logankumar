#dictinoaries
a = {

    "home" : "eswaran",
    "office"   : 22,
    "class" : "python"
    }
print (a)
#acces values
print (a["office"])
#same but get
z = a.get("class")
print (z)
#change
a["home"] = "logan"
print (a)
for x in a:
    print (x)
#keys method
z =a.keys()
print (z)
#values
for x in a:
    print(a[x])
#value m
for x in a.values():
    print (x)
#items
for x,y in a.items():
    print (x,y)
if "office" in a:
    print ("ya")
#setdefault
z =a.setdefault("car","sk")
print (a)
#add
a["mk"]="yes"
print (a)
#update()
a.update({"loga": 12})
print (a)
#remove
#a.pop()
#print (a)
print (a.pop("car"))
print (a)
#del
del a["mk"]
print (a)
#clear()
#a.clear()
#print (a)
#copy constructor
z =dict(lk = 5 ,ls = 10)
print (z)
#happy
print ("happy")








