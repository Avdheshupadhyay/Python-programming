d1={}
n=int(input("size="))
for i in range(n):
    key=eval(input("keys="))
    value=eval(input("values="))
    d1.update({key:value})
print(d1)
l1=[]
for i in d1.keys():
    l1.append(i)
print(l1.sort())
    
