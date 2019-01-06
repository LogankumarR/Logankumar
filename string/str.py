a= "string"
print(a)
print (a[1])
print (a[-1])
print (a[2:4])
print (len(a))

#concatination
a="hai"
b='logan'
print (a+b)
#repetation
print (a*2)
print(a*5)
print (len(a))
a='logan'
print (a.upper())
print (a)
b="HELLO"
print (b.lower())
#replace
a='hai is is logan'
print (a.replace('is','was'))
print (a.replace('is','was',1))
#strip
a= "     logan hi"
print(a.strip())
a="hai logan hai "
a='hai logan hai'
b = "log log log"
print (b.rstrip("log"))
c= "my name is mine"
print (c.lstrip("my)"))
a="            hai       hai    hai      "
print (a.strip())
a="llllllllllhailllllllllhaillllllll"
print (a.strip("l"))
#split
a="logan in as python"
print (a.split())
print (a.split(', '))
b="hai,   logan,logan  "
print (b.split(",  "))
b="lk, mk, dk"
print(b.split(", "))
print (b.split(", ", 1))
