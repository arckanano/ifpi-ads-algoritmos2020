#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <math.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int a, b, c;
    float r1, r2, delta;

    printf("A | B | C\n");
    scanf("%d%d%d", &a, &b, &c);

    delta = (pow(b, 2) - (4 * a * c));
    r1 = ((b * -1) + sqrt(delta)) / (2 * a);
    r2 = ((b * -1) - sqrt(delta)) / (2 * a);

    printf("Raiz 1: %f\nRaiz 2: %f", r1, r2);
    
    system("pause");
    return 0;

}// Erro na execution