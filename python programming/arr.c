#include<stdio.h>
void main()
{
    int m,i,j;
    printf("ENTER THE ORDER OF MATRIX: ");
    scanf("%d",&m);
    int a[m][m];
    for(i=0;i<m;i++){
        printf("ENTER THE ELEMENT: ");
        scanf("%d",&a[i][0]);
    }
    for(i=0;i<m;i++){
        for(j=0;j<m;j++){
        printf("%d ",a[i][j]);
        }
    }
}

    

    