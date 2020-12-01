#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int la, lb, lc;

    printf("Lado1 | lado2 | lado3\n");
    scanf("%d%d%d", &la, &lb,&lc);

    // Verificar se formam um triangulo; a soma de 2 lados não pode ser menor que o terceiro lado;
    int laplb = la + lb;
    int lbplc = lb + lc;
    int lcpla = lc + la;

    if ( (laplb < lc) || (lbplc < la) || (lcpla < lb) || (la == 0) || (lb == 0) || (lc == 0)) {
        printf("Não é triangulo.");
    } else {
        if ( (la == lb) && (la == lc) ) {
            printf("Equilatero");
        } else if ( (la == lb) || (lb == lc) || (lc == la)) {
            printf("Isosceles");
        } else {
            printf("Escaleno");
        }
    }
    
    system("pause");
    return 0;

}