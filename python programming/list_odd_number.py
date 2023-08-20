d=[]
n=int(input("limit="))
l=[]
for i in range(1,n+1):
    d.append(i)
for i in d:
    if i%2!=0:
        l.append(i)
print(l)
        