#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int n, divisor=0;

    printf("N: ");
    scanf("%d", &n);

    for ( i = 1; i <= n; i++)
    {
        if ( n % i == 0) {
            divisor += 1;
        }
    }
    
    if (div == 2) {
        printf("é primo");
    } else {
        printf("Não é primo");
    }
    
    system("pause");
    return 0;

}