    
    while n!=1 and n!=0:
        l.append(n%2)
        n=n//2
    else:
        l.append(1)
    t=[print(i,end='') for i in l[::-1]]
    