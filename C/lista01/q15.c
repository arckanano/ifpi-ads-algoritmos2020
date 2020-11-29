#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    float tempC, tempF;

    printf("Temperatura em F = ");
    scanf("%f", &tempF);

    tempC = (5 * tempF - 160) / 9;

    printf("Temperatura de C = %f", tempC);
    
    system("pause");
    return 0;

}