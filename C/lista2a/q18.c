#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void)
{

    setlocale(LC_ALL, "");

    float a, b, soma, sub, mult, div;
    int op;

    printf("VAL1 | VAL2\n");
    scanf("%f%f", &a, &b);

    printf("1 - SOMA\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n");

    soma = a + b;
    sub = a - b;
    mult = a * b;
    div = a / b;

    printf("Opção: ");
    scanf("%d", &op);

    switch (op)
    {
    case 1:
        // soma
        printf("%0.2f", soma);
        break;
    case 2:
        // subtração
        printf("%0.2f", sub);
        break;
    case 3:
        // multiplicação
        printf("%0.2f", mult);
        break;
    case 4:
        // divisão
        printf("%0.2f", div);
        break;

    default:
        break;
    }

    system("pause");
    return 0;
}