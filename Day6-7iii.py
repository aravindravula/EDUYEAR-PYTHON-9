a=[1,4,9,6,8]
if a==a[::-1]:
  
   print("palindrome")

else:
    
    print("not palindrome") 
a.sort()
print("maximum number:",a[-1]) 
print("minimum number:",a[0]) 