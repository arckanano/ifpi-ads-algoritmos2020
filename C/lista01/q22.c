#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int minutos, totDias, totHoras, totMinutos;

    printf("Minutos = ");
    scanf("%d", &minutos);

    // 1 dia tem 1440 minutos;
    totDias = minutos / 1440;

    totHoras = (minutos % 1440) / 60;

    totMinutos = (minutos % 1440) % 60;

    printf("%d Minutos = %d Dias, %d Horas, %d Minutos", minutos, totDias, totHoras, totMinutos);
    
    system("pause");
    return 0;

}