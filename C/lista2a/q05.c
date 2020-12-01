#include <stdio.h>

int main(void)
{
    int a, b, c;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    if (a > b)                                           // a>b
        if (b > c) printf("%4d%4d%4d\n", a, b, c);       // a>b>c
        else                                             // a>b,c>=b
            if (a > c) printf("%4d%4d%4d\n", a, c, b);   // a>c>=b
            else printf("%4d%4d%4d\n", c, a, b);         // c>=a>b
    else                                                 // b>=a
        if (b > c)                                       // b>=a,b>c
            if (a > c) printf("%4d%4d%4d\n", b, a, c);   // b>=a>c
            else printf("%4d%4d%4d\n", b, c, a);         // b>c>=a
        else printf("%4d%4d%4d\n", c ,b, a);             // c>=b>=a
    return 0;
}
