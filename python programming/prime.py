x=int(input("enter the any number="))
i=2
flag=0
while i<=x-1:
    if x%i==0:
        flag=flag+1
    i=1+1
if flag==0:
    print("prime number:")
else:
    print("not prime number:")

