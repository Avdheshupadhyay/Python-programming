def prime(l):
    for i in range(2,l):
        if(l%i==0):
            return False
    return True
l=[2,3,4,5,6,7,8,9,10]
print(list(filter(prime,l)))