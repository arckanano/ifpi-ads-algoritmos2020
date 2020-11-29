#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    float valorReal, fracao;

    printf("Valor em Real: ");
    scanf("%f", &valorReal);

    fracao = (valorReal / 100) * 70;

    printf("resultado: %0.2f \n", fracao);
    
    system("pause");
    return 0;

}