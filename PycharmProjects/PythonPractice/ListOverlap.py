a=[1,6,45,364]
b=[6,23,76,23,364]
new=[]


for i in a:
    if i in b:   new.append(i)

print(new)