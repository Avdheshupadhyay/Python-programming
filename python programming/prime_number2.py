x=int(input("enter the number="))
i=2
c=0
while i<x:
    if x%i==0:
        c+=1
    i+=1
if c==0:
    print("the number is prime:")
else:
    print("not prime:")