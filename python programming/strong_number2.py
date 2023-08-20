import math
sum=0
n=int(input("enter the any number="))
temp=n
 for i in str(n):
     x=math.factorial(int(i))
     sum+=x
if(n==sum):
    print("strong number:")
else:
    print("not")

     
 