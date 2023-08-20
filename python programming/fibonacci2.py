T=int(input("enter the n term="))
n1=0
print(n1,end=" ")
n2=1
print(n2,end=" ")
for i in range(2,T):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3
    n3=n1
    
    

