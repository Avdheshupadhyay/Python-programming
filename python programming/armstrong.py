n=int(input("enter the number="))
temp=n
b=len(str(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+r**b
    n=n//10
if sum==temp:
    print("this number is armstrong:")
else:
    print("not armstrong:")

