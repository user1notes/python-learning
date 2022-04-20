print("hello")

x = "hello"
print(x,type(x))
x=3
print(x,type(x))
x=20.0
print(x,type(x))
x=1j
print(x,type(x))
x = ["apple", "banana", "cherry"]
print(x,type(x))

#Tuples
x = ("apple", "banana", "cherry")

#accessing tuples
print(x[1])
print(x[0:2])
print(x,type(x))

#updating tuples
y = list(x)
y[1] = "orange"
x = tuple(y)
y = list(x)
y.append("fruit1")
x = tuple(y)
print(x)
y = ("fruit2",)
x = x + y
print(x)

#unpacking tuples
(a,b,c,d,e) = x
print(a)
print(b)
print(c)

#finding index
print(x.index("fruit1"))

