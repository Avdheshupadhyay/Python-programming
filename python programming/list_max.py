l=[]
n=int(input("size="))
for j in range(0,n):
    a=int(input("element="))
    l.append(a)
max=0
temp=1
for i in range(0,n):
    max=l[0]
    if max<l[i]:
        temp=max
        max=l[i]
        l[i]=temp
print(max)
