L=[]
for i in range(6):
    l=list(map(int,input().split()))
    L.append(l)
mx_sum=0
for i in range(4):
    for j in range(4):
        sumat=L[i][j]+L[i][j+1]+L[i][j+2]+L[i+1][j+1]+L[i+2][j]+L[i+2][j+1]+L[i+2][j+2]
        if sumat>mx_sum:
            mx_sum=sumat
print(mx_sum)