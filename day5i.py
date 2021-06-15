count=0
sum=0
while True:
    user_input=input("enter a number:")
    if user_input=='q':
        break
    user_input=int(user_input)
    sum=sum+user_input
    count=count+1
    print(sum)
