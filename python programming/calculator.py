a=int(input("enter the value of a="))
b=int(input("enter the value of b="))
sign=int(input("enter the operator for calc="))
# 1 =+\\2=-\\3=*\\4=/
if sign==1:
    print(a+b)
elif sign==2:
    print(a-b)
elif sign==3:
    print(a*b)
elif sign==4:
    print(a/b)