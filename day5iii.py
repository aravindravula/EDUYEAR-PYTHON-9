n=int(input("enter a number:"))
m=int(input("enter a number:"))
for i in range(n,m+1):
    if(i%5==0 and i%7==0):
        print(i)
