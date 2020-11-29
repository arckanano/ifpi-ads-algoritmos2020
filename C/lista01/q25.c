#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int dias, totAnos, totMeses, totDias;

    printf("Dias = ");
    scanf("%d", &dias);

    totAnos = dias / 365;

    totMeses = (dias % 365) / 30;

    totDias = (dias % 365) % 30;

    printf("%d Dias = %d Anos, %d Meses, %d Dias.", dias, totAnos, totMeses, totDias);
    
    system("pause");
    return 0;

}