d={}
n=int(input("size="))
for i in range(n):
    key=eval(input("key="))
    value=eval(input("value="))
    d.update({key:value})
#print(d.items())
for i in d:
    print(i)
print(d[1])
d.update({1:2888776})
print(d)