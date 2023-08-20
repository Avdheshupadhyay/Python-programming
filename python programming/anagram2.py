x=input("enter the first string=").lower()
y=input("enter the second string=").lower()
c=0
if len(x)==len(y):
    
    for i in x:
        for j in y:
           if i==j:
               c+=1
    if c==len(x):
        print("anagram")
    else:
        print("not")
else:
    print("not")

