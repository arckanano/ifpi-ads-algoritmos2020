#include <stdio.h>

main() {

    float dolarHoje;
    float valDolar;
    float resReal;

    printf("Valor dolar hoje: ");
    scanf("%f", &dolarHoje);

    printf("Valor em dolar: ");
    scanf("%f", &valDolar);

    resReal = valDolar * dolarHoje;

    printf("\n%f Dolar em Real = %0.2f", valDolar, resReal);

    return 0;
}