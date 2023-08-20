d={}
n=int(input("no. of student="))
for  i in range(1,n+1):
    key=eval(input("roll no.="))
    value=eval(input("biodata="))
    d.update({key:value})
    
search=eval(input("search roll no.="))
for i in d.keys():
    if i==search:
        print(d[search])
