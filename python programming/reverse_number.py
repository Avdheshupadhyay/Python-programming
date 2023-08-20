x=int(input("enter the any number"))
  temp=x
sum=0
while x>0:
r=x%10
sum=(sum*10)+r
n=n%10
if(sum==temp):
    print("this number is palindrom")
else:
    print("this number is not palindrom:")
