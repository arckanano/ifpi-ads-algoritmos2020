#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int dia, mes, ano;

    printf("DIA | MES | ANO\n");
    scanf("%d%d%d", &dia, &mes, &ano);

    if ( (dia > 0) && ( dia <31)) {
        if ( ( mes > 0) && (mes < 13)) {
            if ( (ano > 0) && (ano <= 2020)) {
                printf("%d-%d-%d é válido", dia, mes, ano);
            } else {
                printf("Data inválida");
            }
        } else {
            printf("Data Inválida");
        }
    } else {
        printf("Data inválida!");
    }
    
    system("pause");
    return 0;

}