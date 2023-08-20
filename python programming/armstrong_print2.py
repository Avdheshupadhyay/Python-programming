def armstrong(n):
    temp=n
    c=0
    for i in str(n):
        c=c+int (i)**3
    if c==temp:
        return c
l=[]
for i in range(100,1000):
    l.append(i)
print(tuple(filter(armstrong,l)))
    
        
        