n=int(input("enter the any number="))
sum=0
temp=n
b=len(str(n))
while n!=0:
    r=n%10
    sum=sum+(r**b)
    n=n//10
if temp==sum:
    print("armstrong:")
else:
    print("not:")
