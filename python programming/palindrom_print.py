def palindrom(n):
    if str(n) ==str(n)[::-1]:
        return int(n)
  
l=[]
for i in range(100,1000):
    l.append(i)
    
print(list(filter(palindrom,l)))