n=int(input("enter the any number="))
c=0
i=2
while i<n:
    if n%i==0:
        c+=1
    i+=1

if c==0:
    print("prime number:")
else:
    print("not:")