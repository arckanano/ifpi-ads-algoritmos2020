#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int entradaMetros, saidaKM, saidaMetros;

    printf("Metros = ");
    scanf("%d", &entradaMetros);

    saidaKM = entradaMetros / 1000;
    saidaMetros = entradaMetros % 1000;

    printf("%d equivale a %d KM e %d M", entradaMetros, saidaKM, saidaMetros);
    
    system("pause");
    return 0;

}