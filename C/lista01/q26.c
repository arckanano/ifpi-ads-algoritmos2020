#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <math.h>

int main(void)
{

    setlocale(LC_ALL, "");

    int anosFumando, cigarrosDia;
    float valorGasto, diasFumando, totCigarros, totCarteiras, valorCarteira;

    printf("Anos fumando: ");
    scanf("%d", &anosFumando);
    printf("Número de cigarros por dia: ");
    scanf("%d", &cigarrosDia);
    printf("Preço da carteira: ");
    scanf("%f", &valorCarteira);

    diasFumando = anosFumando * 365;
    totCigarros = diasFumando * cigarrosDia;
    totCarteiras = ceil(totCigarros / 20);

    valorGasto = totCarteiras * valorCarteira;

    printf("%f %f %f %f", diasFumando, totCigarros, totCarteiras, valorGasto);

    system("pause");
    return 0;
}