n=int(input("enter the any number="))
temp=n
sum=0
while (n>0):
    r=n%10
    sum=(sum*10)+r
    n=n//10
if (temp==sum):
    print("this number is palindrom")
