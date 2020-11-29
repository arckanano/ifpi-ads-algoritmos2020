#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int anos, meses, dias, totdias;

    printf("Anos | Meses | Dias");
    scanf("%d%d%d", &anos,&meses,&dias);

    totdias = (anos * 365) + (meses * 30) + dias;

    printf("Total de dias = %d", totdias);
    
    system("pause");
    return 0;

}