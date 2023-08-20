d=[]
n= int(input("range="))
for j in range(1,n+1):
    d.append(j)
m=[]
c=0
for i in d:
    if i%2==0:
        m.append(i)
         
print(m)