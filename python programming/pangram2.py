x=input("enter the any string=")
y=x.lower()
for i in range(97,123):
    if chr(i) not in y:
        print("not pangram")
        break
else:
    print("pangram") 

