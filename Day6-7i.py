a=[111,131,151,10] 
c=0 
for i in a:
    temp=i
    rev=0
    while temp>0:
        rev=rev*10+temp%10
        temp=temp//10
        if rev==i:
            print(i)
            c=c+1 
            
        