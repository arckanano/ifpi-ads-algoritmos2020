#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    float meuSalario, novoSalario;

    printf("Meu salário: ");
    scanf("%f", &meuSalario);

    novoSalario = meuSalario * 1.25;

    printf("Salário atual: %0.2f\nValor do aumento: %0.2f\nNovo salário: %0.2f", meuSalario, novoSalario);
    
    system("pause");
    return 0;

}