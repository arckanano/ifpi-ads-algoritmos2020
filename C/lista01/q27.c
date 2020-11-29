#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    float custoCarro, percFabrica=0.28, impostos=0.45, valorCarro;

    printf("Custo do carro = ");
    scanf("%f", &custoCarro);

    valorCarro = custoCarro + (custoCarro * percFabrica) + (custoCarro * impostos);

    printf("Valor total do carro: %0.2f", valorCarro);
    
    system("pause");
    return 0;

}