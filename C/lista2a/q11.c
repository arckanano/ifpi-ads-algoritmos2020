#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void)
{

    setlocale(LC_ALL, "");

    int option, num1, num2, num3;

    printf("N1 - n2 - n3\n");
    scanf("%d%d%d",&num1, &num2, &num3);

    printf("Aopção:");
    scanf("%d", &option);

    switch (option)
    {
    case 1:
        printf("%d", num1);
        break;
    case 2:
        printf("%d", num2);
        break;
    case 3:
        printf("%d", num3);
        break;
    default:
        printf("Valor inválido!");
        break;
    }

    system("pause");
    return 0;
}