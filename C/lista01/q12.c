#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    float raio, pi=3.14, comprimento;

    printf("Raio:\n")
    scanf("%f", &raio);

    comprimento = 2 * pi * raio;

    printf("Comprimento = %0.2f", comprimento);
    
    system("pause");
    return 0;

}