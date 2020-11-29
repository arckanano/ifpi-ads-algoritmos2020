#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

int main(void) {

    setlocale(LC_ALL, "");
    
    int valorSaque, qtd50, qtd20, qtd10, qtd5, qtd2;

    printf("valor do saque: ");
    scanf("%d", &valorSaque);

    // qtd notas de 50;
    qtd50 = valorSaque / 50;
    // qtd notas de 20;
    qtd20 = (valorSaque % 50) / 20;
    // qtd notas de 10;
    qtd10 = ((valorSaque % 50) % 20) / 10;
    // qtd notas de 5;
    qtd5 = (((valorSaque % 50) % 20) % 10) / 5;
    // qtd notas de 2;
    qtd2 = ((((valorSaque % 50) % 20) % 10) % 5) / 2;

    // Resultado
    printf("SAQUE\n%d Notas de 50\n%d Notas de 20\n%d Notas de 10\n%d Notas de 5\n%d Notas de 2", qtd50, qtd20, qtd10, qtd5, qtd2);
  
    system("pause");
    return 0;

}