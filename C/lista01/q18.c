#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int valorKg, valorG;

    printf("Valor em KM = ");
    scanf("%d", &valorKg);

    valorG = valorKg * 100;

    printf("%d metros = %d centímetros", valorKg, valorG);
    
    system("pasue");
    return 0;

}