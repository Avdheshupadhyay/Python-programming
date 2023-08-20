# simpel calculator in python programming
x=int(input("enter the first number = "))
y=int(input("enter the second number ="))
code=int(input("enter the code // hint : 1=+ ,2=- ,3=* ,4=/ :-> "))
if code==1:
    print("the sum of two number is =",x+y)
elif code==2:
    print("the substract of two number is =",x-y)
elif code==3:
    print("the product of two number is =",x*y)
elif code==4:
    print("the divide of two number is =",x/y)
else:
    print("please enter the valid code :")

