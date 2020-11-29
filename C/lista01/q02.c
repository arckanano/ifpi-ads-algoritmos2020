#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");

    float dolarHoje;
    float valDolar;
    float resReal;

    printf("Valor dolar hoje: ");
    scanf("%f", &dolarHoje);

    printf("Valor em dolar: ");
    scanf("%f", &valDolar);

    resReal = valDolar * dolarHoje;

    printf("\n%f Dolar em Real = %0.2f", valDolar, resReal);

    system("pause");
    return 0;
}