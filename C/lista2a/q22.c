#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int minInicio, horaInicio, inicioEmMin, minFim, horaFim, fimEmMin, tempoJogo, totMinDia=1440, dMin, dHora, tempo1, tempo2;

    printf("Hora Inicial | Minuto Inicial\n");
    scanf("%d%d", &horaInicio, &minInicio);
    printf("Hora Fim | Minuto Fim\n");
    scanf("%d%d", &horaFim, &minFim);

    inicioEmMin = minInicio + (horaInicio * 60);
    fimEmMin = minFim + (horaFim * 60);

    if (inicioEmMin < fimEmMin) {
        tempoJogo = fimEmMin - inicioEmMin;
        dHora = tempoJogo / 60;
        dMin = tempoJogo % 60;
        printf("Duração: %d Horas e %d minutos", dHora, dMin);
    } else {
        tempo1 = totMinDia - inicioEmMin;
        tempo2 = fimEmMin;
        tempoJogo = tempo1 + tempo2;
        dHora = tempoJogo / 60;
        dMin = tempoJogo % 60;
        printf("Duração: %d Horas e %d minutos", dHora, dMin);
    }

    system("pause");
    return 0;

}