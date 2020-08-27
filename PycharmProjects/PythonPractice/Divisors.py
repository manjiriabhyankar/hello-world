Number=int(input("Enter one number\n"))

x=list(range(2,Number+1))
less=[]
for i in x:
    if Number%i==0:
        less.append(i)

print(less)