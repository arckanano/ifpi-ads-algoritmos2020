#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int n;

    printf("N: ");
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("Par");
    } else {
        printf("Ímpar");
    }
    
    system("pause");
    return 0;

}