import math
n=int(input("enter the any number:"))
sum=0
temp=n
while n!=0:
    r=n%10
    x=math.factorial(r)
    sum=sum+x
    n=n//10
if temp==sum:
    print("strong number:")
else:
    print("not")
    