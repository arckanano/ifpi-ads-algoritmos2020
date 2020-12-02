#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <math.h>


int main(void) {

    setlocale(LC_ALL, "");
    
    int val1, val2, restoDiv, pot1, pot2, soma2;
    printf("Valores: ");
    scanf("%d%d", &val1, &val2);

    pot1 = pow(val1, 2);
    pot2 = pow(val2, 2);

    soma2 = val1 + val2;
    restoDiv = val1 % val2;

    int caso1 = soma2 + restoDiv;
    int caso3 = soma2 * val1;
    float caso4 = soma2 / val2;

    if (restoDiv == 1) {
        printf("Soma dos valores + resto: %d", caso1);
    } else if ( restoDiv == 2) {
        if (val1 % 2 == 0) {
            printf("Valor 1 é PAR\n");
        } else {
            printf("Valor 1 é IMPAR\n");
        }
        if (val2 % 2 == 0) {
            printf("Valor 2 é PAR\n");
        } else {
            printf("Valor 2 é IMPAR\n");
        }
    } else if ( restoDiv == 3) {
        printf("\n%d", caso3);
    } else if ( restoDiv == 4 ) {
        printf("\nDivisão da soma pelo segundo %0.2f", caso4);
    } else {
        printf("\nPotencia do valor 1: %d\nPortencia do valor 2: %d", pot1, pot2);
    }
    system("pause");
    return 0;

}