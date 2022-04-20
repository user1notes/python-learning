s = {"apple", "banana", "cherry"}
print(s)

#duplicates are ignored
s = {"apple", "banana", "cherry", "apple"}
print(s)

#access set items
for x in s:
    print(x)

#add items in set
s.add("orange")
print(s)

s1 = {"fruit1", "fruit2"}
s.update(s1)
print(s)

s2 = ["fruit2", "fruit3"]
s.update(s2)
print(s)

#remove from set
s.remove("banana")
print(s)

#union of two sets returns a new set
s2 = {"fruit4", "fruit5"}
s3 = s1.union(s2)
print(s3)

#this won't generate error
s.discard("banana")
print(s)

#clear set
s.clear()
print(s)

del s
