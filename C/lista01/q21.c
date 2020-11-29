#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int meses, totMeses, totAnos;

    printf("Meses = ");
    scanf("%d", &meses);

    totAnos = meses / 12;
    totMeses = meses % 12;

    printf("%d Meses = %d anos e %d meses", meses, totAnos, totMeses);
    
    system("pause");
    return 0;

}