#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int entradaHoras, horasSemana=7*24, totSemanas, totDias, totHoras;

    printf("Hotas = ");
    scanf("%d", &entradaHoras);

    // Total de horas na Semana
    totSemanas = entradaHoras / horasSemana;
    // Total de dias
    totDias = entradaHoras % horasSemana;
    // Total de horas
    totHoras = (entradaHoras % horasSemana) / 24;

    printf("%d horas = %d semanas %d dias e %d horas", entradaHoras, totSemanas, totDias, totHoras);
    
    system("pause");
    return 0;

}