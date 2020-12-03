#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    float angulo;

    printf("Angulo: ");
    scanf("%f", &angulo);

    if ( (angulo >= 0) && (angulo < 90)) {
        printf("Quadrante 1");
    } else if (( angulo >= 90) && (angulo < 180)) {
        printf("Quadrante 2");
    } else if ( (angulo >= 180) && (angulo < 270)) {
        printf("Quadrante 3");
    } else if ( (angulo >= 270) && (angulo <= 360)) {
        printf("Quadrante 4");
    } else {
        printf("INVALIDO");
    }
    
    system("pause");
    return 0;

}