a="logan"
print (a[0])
print (a[-1])
print (a[-2])
# d print (a[1:5])
print (a[1:4])
print (len(a))
print (len(a))
print (a.upper())
print (a)
b='LOGAN'
print (b.lower())
a='logan was at was loga'
print (a.replace('was','is'))
print (a.replace('was','is',2))
c='    hai logan                 '
print (c.strip())
c="hai0000hai0000hai"
print (c.strip("hai"))
print (c.lstrip("hai"))
print (c.rstrip("hai"))
# split
a="hai logan how are u "
print (a.split())
b="hai, is,logan "
print (b.split(","))
c="hai, logan ,wat ,doing"
print (c.split(",", 3))
#starts with
s = "hai is am logan kumar"
print (s.startswith("hai"))
print (s.startswith("i"  , 4 , 9))
#ends with
h = "hai am logan kumar."
print (h.endswith("r."))
print (h.endswith("am,2,4"))
#islower
a = "hai i am Logan"
print (a.islower())
#isupper
a = 'hai i am python'
print (a.isupper())
j = 'LOGAN !123456'
print (j.isupper())
#in ,not in
l = "isksi"
print ("s" in l)
print ("i" not in l)