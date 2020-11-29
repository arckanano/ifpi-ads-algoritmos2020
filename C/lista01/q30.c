#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void)
{

    setlocale(LC_ALL, "");

    int valProd, entrada, parcelas, sobra;

    printf("Valor do Produto: ");
    scanf("%d", &valProd);

    sobra = valProd % 3;
    entrada = (valProd / 3) + sobra;
    parcelas = (valProd - entrada) / 2;

    printf("Entrada de %d\nParcela 1 = %d\nParcela 2 = %d", entrada, parcelas, parcelas);

    system("pause");
    return 0;
}