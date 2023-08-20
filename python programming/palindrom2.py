n=int(input("enter the any number="))
sum=0
temp=n
while n!=0:
    r=n%10
    sum=(sum*10)+r
    n=n//10
if temp==sum:
    print("this number is palindrom:")
else:
    print("not:")
    

