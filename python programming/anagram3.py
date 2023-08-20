x=input("enter the first string=").lower()
y=input("enter the second string=").lower()
if sorted(x)==sorted(y):
    print("anagram")
else:
    print("not anagram")