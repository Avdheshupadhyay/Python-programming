def list1():
    l=[]
    n=int(input("size="))
    for i in range(1,n):
        element=eval(input("element="))
        l.append(element)
    sum=0
    for i in l:
      sum=sum+i
    return sum
print(list1())