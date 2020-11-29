#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    float kiloLatao, cobre=0.70, zinco=0.30, totCobre, totZinco;

    printf("Kilos de Latão: ");
    scanf("%f", &kiloLatao);

    totCobre = kiloLatao * cobre;
    totZinco = kiloLatao * zinco;

    printf("%f Kilos de Latão = %0.2f Kilos de Zinco + %0.2f Kilos de Cobre", kiloLatao, totZinco, totCobre);
    
    system("pause");
    return 0;

}