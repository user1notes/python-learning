i = 1
while(i<6):
    print(i)
    i += 1 

print()
i = 1
#break in while
while(i<6):
    print(i)
    if(i==4):
        break
    i += 1

print()
i = 0
#continue
while(i<6):
    i += 1
    if(i==4):
        continue
    print(i)

print()    
i = 1
#while with else
while(i<6):
    print(i)
    i += 1
else:
    print("i is greater than 5 now")
