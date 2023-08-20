n1=int(input())
n2=int(input())
flg=0
if(n1<n2):
    sml=n1
else:
    sml=n2
if flg:
    for i in range(sml,(n1*n2)+1):
        if i%n1==0 and i%n2==0:
            print(i)
            break
