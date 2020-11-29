#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int base, altura;
    float area;

    printf("BASE | ALTURA\n");
    scanf("%d %d", &base, &altura);

    area = base * altura;

    printf("Area = %f", area);
    
    system("pause");
    return 0;

}