#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void)
{

    setlocale(LC_ALL, "");

    int n1, dezena, unidade;

    printf("Número de 2 dígitos: ");
    scanf("%d", &n1);

    dezena = n1 / 10;
    unidade = n1 % 10;

    if (dezena == unidade)
    {
        printf("São iguais.");
    }
    else
    {
        printf("São diferentes.");
    }

    system("pause");
    return 0;
}