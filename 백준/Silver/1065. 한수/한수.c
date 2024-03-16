#include <stdio.h>

int hansoo(int n)
{
    int i = 0, check = 0;
    int tmp[4] = {0};
    while(n)
    {
        tmp[i] = n%10;
        n/=10;
        i++;
    }
    if(i<3) return 1;
    else
    {
       for(int j = i-1; j>1; j--)
       {
           if(tmp[j]-tmp[j-1] == tmp[j-1]-tmp[j-2]) check = 1;
           else 
           {
               check = 0;
               break;
           }
       }
    }
    if(check == 0) return 0;
    else return 1;
}


int main()
{
    int n, count = 0;
    scanf("%d", &n);
    int N[1001] = {0};
    for(int i = 1; i<=n; i++)
    {
        N[i] = hansoo(i);
        if(N[i] == 1) count++;
    }
    printf("%d\n", count);
    return 0;
}