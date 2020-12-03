#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    // IMC

    float altura, peso, imc;

    printf("Altura: \n");
    scanf("%f", &altura);

    printf("Peso: \n");
    scanf("%f", &peso);

    imc = peso / (altura * altura);

    if (imc < 25) {
        printf("Peso NORMAL");
    } else if ( (imc >= 25) && (imc <= 30)) {
        printf("OBESO");
    } else if ( imc > 30 ) {
        printf("OBESIDADE MÓBIDA");
    }
    
    system("pause");
    return 0;

}