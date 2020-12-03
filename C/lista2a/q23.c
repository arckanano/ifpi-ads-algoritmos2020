#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int pDia, pMes, pAno, sDia, sMes, sAno, pEmDias, sEmDias;

    printf("Primeira data: ");
    scanf("%d %d %d", &pDia, &pMes, &pAno);
    printf("Segunda data: ");
    scanf("%d %d %d", &sDia, &sMes, &sAno);

    pEmDias = (pAno * 365) + (pMes * 30) + pDia;
    sEmDias = (sAno * 365) + (sMes * 30) + sDia;

    if (pEmDias > sEmDias) {
        printf("Primeira data é mais recente");
    } else {
        printf("Segunda data é mais recente");
    }
    
    
    system("pause");
    return 0;

}