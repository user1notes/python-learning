a = 3
b = 4
c = 5

if(a>b):
    if(a>c):
        print("greatest is: a-",a,end="")

if(b>a):
    if(b>c):
        print("greatest is: b-",b,end="")

if(c>a):
    if(c>a):
        print("greatest is: c-",c,end="")

print()
#using elif, and
if(a>b and a>c):
    print("gretest a ",a,end="")
if(b>a and b>c):
    print("gretest b ",a,end="")
else:
    print("greatest c",c,end="")

#pass does nothing
if(c>b):
    pass
