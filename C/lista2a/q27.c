#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int nascDia, nascMes, nascAno, atualDia, atualMes, atualAno, totDiasNasc, totDiaDataAtual, diasDeVida;

    printf("Data de nascimento (DD MM AAAA)");
    scanf("%d%d%d", &nascDia, &nascMes, &nascAno);
    printf("Data Atual (DD MM AAAA)");
    scanf("%d%d%d", &atualDia, &atualMes, &atualAno);

    totDiasNasc = nascDia + (nascMes * 30) + (nascAno * 365);
    totDiaDataAtual = atualDia + (atualMes * 30) + (atualAno * 365);

    diasDeVida = totDiaDataAtual - totDiasNasc;

    
    
    system("pause");
    return 0;

}