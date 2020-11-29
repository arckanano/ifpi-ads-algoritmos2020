#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    float tempC, tempF;

    printf("Temperatura de C = ");
    scanf("%f", &tempC);

    tempF = (9 * tempC + 160) / 5;

    printf("Temperatura de F = %0.2f", tempF);
    
    system("pause");
    return 0;

}