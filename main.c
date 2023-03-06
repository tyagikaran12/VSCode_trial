#include <stdio.h>
#include<conio.h>

int main()
{
    int i,j;
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=8;j++)
        {
            if(j<=i || j+i>8)
            {
                printf("* ");
            }
            
            else
            {
                printf("  ");
            }
        }
        printf("\n");
    }
}