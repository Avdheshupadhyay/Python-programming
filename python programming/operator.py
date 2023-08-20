i=int(input("enter the starting number"))
lim=int(input("enter the limit="))
sum=0
if i%2==0:
    while i<=lim:
        sum+=i
        i+=2
print("the sum of even numbers=",sum)  
elif i%2==1:
    i=i+1
    while i<=lim:
        sum+=i
        i+=2
print("the sum is=",sum)
else:
    print("something went wrong:")
    
  
    